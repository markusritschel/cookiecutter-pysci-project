# AGENTS.md

This file provides guidance to coding agents working in this repository.

## What this repository is

A **[Copier](https://copier.readthedocs.io) template** for scientific Python projects (migrated from cookiecutter/cruft — the repo name is historical). Nothing here is a library to import: the deliverable is the _generated_ project. Two audiences live side by side:

- **The template itself** — `copier.yml` (questions/tasks/migrations), `template/` (the rendered files), `tasks/post_gen.py`, `scripts/`.
- **The docs site** about the template — `docs/`, `zensical.toml`, `overrides/`, built with Zensical and deployed to GitHub Pages.

`pyproject.toml` at the root declares only the tooling needed to _test_ the template (copier, jinja2-time, pytest). The generated project's dependencies live in `template/pyproject.toml.jinja`.

## Commands

**Generate a project locally from the working tree** (the primary way to test a change):

```bash
uvx --with jinja2-time copier copy --defaults --trust --vcs-ref HEAD . /tmp/test-project
```

- `--trust` is mandatory — the template runs `_tasks` and uses the `jinja2-time` extension.
- `--vcs-ref HEAD` is mandatory for a local source: copier otherwise generates from the latest **git tag**, silently ignoring uncommitted/unpushed template changes.
- Drop `--defaults` to answer questions interactively; useful to exercise the `docs_engine` / `is_research_project` / `command_line_interface` branches.

**Run the template repo's own tests** (they cover `scripts/migrate_cookiecutter_to_copier.py` only, and are _not_ run in CI):

```bash
uv run pytest scripts/ -q
uv run pytest scripts/ -k test_load_cruft_context_drops_underscore_keys   # single test
```

Don't run a bare `uv run pytest` from the root — it collects any generated test project lying around (e.g. an untracked `my-code-base/`).

**Verify a generated project** — mirror the CI steps inside the generated directory:

```bash
uv sync --locked --dev && uv run ruff check . && uv run pytest -v
```

**Build the docs site for this repo** (Zensical is not a declared dev dependency here):

```bash
uvx zensical serve    # live reload
uvx zensical build --clean
```

CI (`.github/workflows/main.yml`) does exactly one thing: generate with `--defaults` on Python 3.10 and 3.12, then install/lint/test the result. A template change is only verified once that pipeline is green — rendering successfully is not enough.

## Architecture

### Rendering contract

`_subdirectory: template` and `_templates_suffix: ".jinja"` mean:

- A file **with** `.jinja` is rendered and the suffix stripped. A file **without** it is copied verbatim — so `template/.pre-commit-config.yaml` and `template/conftest.py` cannot contain Jinja.
- **Path names are always rendered**, suffix or not. This is how the template does conditional generation, and it produces the deliberately grotesque filenames in `template/`:
  - `template/{% if is_research_project %}notebooks{% endif %}/…` — an empty-string directory name collapses the whole subtree away.
  - `template/{% if docs_engine|lower == 'sphinx' %}conf.py{% endif %}.jinja` — engine-specific files.
  - `template/{{ package_name }}/…`, `template/{{ _copier_conf.answers_file }}.jinja` — answer-derived names.

Only question answers and the `_copier_*` variables listed in `copier/_main.py:_render_context` (`_copier_answers`, `_copier_conf`, `_folder_name`, `_copier_python`, `_copier_phase`) are in scope during rendering. An **undefined** variable in a path condition fails silently: the condition is falsy, the stem renders to the empty string, and the file is dropped without a warning — see the `_copier_operation` trap below. `tests/test_generation.py` guards against this.

When adding a file, decide deliberately which of these path forms it takes — and whether it also belongs in `_skip_if_exists`.

### Update safety

Two mechanisms, and one trap that looks like a third:

1. **`_skip_if_exists`** (`copier.yml`): user-authored files (`docs/**/*.md`, `**/*.bib`, `tests/**`, `README.md`, `LICENSE`, `CITATION.cff`) plus the example/boilerplate files (`src/*/submodule.py`, `src/*/cli.py`, `notebooks/*.ipynb`, `scripts/*.py`). Written on first copy, never overwritten afterwards.
2. **`_tasks` gated on `when: "{{ _copier_operation == 'copy' }}"`**: post-generation setup runs on `copier copy` only, never on `copier update`. This is the *one* place `_copier_operation` is in scope.
3. ⚠️ **`_copier_operation` (or `_copier_conf.operation`) in a template path or file body — does not work.** copier injects `_copier_operation` only into the context that evaluates `_tasks`/`_migrations` conditions (`copier/_main.py`, `_execute_tasks`); it is undefined during path and content rendering, so the condition is always falsy there. A path guarded that way renders to an empty stem and the file is dropped from *every* generation, `copy` included; a body guarded that way renders empty. Commit 2baedbe did exactly this and silently removed five example files — reverted, with `tests/test_generation.py` as the guard.

Anything mutating the user's project must fall under (1) or (2), or `copier update` will clobber real work. There is no path-level "first generation only" mechanism; `_skip_if_exists` is the closest thing. It does not resurrect a file the user deleted, because `copier update` applies a template-side diff rather than re-rendering the whole tree.

Note what CI cannot see: `pytest` in the generated project collects the doctests in `core/utils.py`, so it exits 0 even with an empty `tests/`. Assert on the generated tree, which is what `tests/` at the repo root does.

### Post-generation (`tasks/post_gen.py`)

Runs once, with CWD set to the generated project, as a standalone Python script (not inline POSIX shell) **so generation works on native Windows without WSL/git-bash** — keep it dependency-free and `subprocess`-based. It: `git init` → branch `main` → commit everything → `git rm --cached` the example files listed in `example_files` → `uv sync --dev` → `pre-commit install` → second commit. `git`/`uv` absence degrades to a printed warning rather than failing.

The `git rm --cached` step is why example files land in the working tree but not in history: the user replaces them instead of inheriting them. `example_files` is keyed off `package_name` (passed as `argv[1]`) and must stay in sync with both the example filenames in `template/` and the example entries in `_skip_if_exists`; `tests/test_generation.py` pins that list.

### Answer-key migrations

`copier.yml` `_migrations` `sed`-rewrites old answer keys (`project_author`→`user_name`, `email`→`user_email`, `github_username`→`github_user`) in `.copier-answers.yml` before an update, so projects generated under the old names keep updating. Renaming a question is therefore a two-part change: the question _and_ a migration entry. `scripts/migrate_cookiecutter_to_copier.py` handles the older cookiecutter/cruft case, mapping `.cruft.json` onto current keys via its own `RENAMED_KEYS`.

### Generated-project shape (what the template promises)

`src/` layout; `BASE_DIR`/`LOG_DIR`/`DATA_DIR`/`PLOT_DIR` exported from the package `__init__` so scripts and notebooks resolve paths from the project root; a `singledispatch` `save()` in `core/utils.py`; `justfile` as the task runner (`just qa`, `just test`, `just docs`); ruff + ty + pytest (`--doctest-modules`, so `src/` docstrings are tests); jupytext triple-format notebook pairing. `template/.claude/CLAUDE.md.jinja` documents all of this for the generated project and is the authoritative description — update it whenever the generated structure changes.

Note `template/justfile.jinja` wraps most of its body in `{% raw %}` because `just` uses `{{ }}` for its own variables; only the `docs_engine` branches (`docs`, `docs-serve`, `clean-docs`) sit outside the raw blocks.

## Conventions

- User-visible changes go in the root `CHANGELOG.md` under `## Unreleased`, recording the _rationale_ and rejected alternatives (see the `tasks/post_gen.py` entry as the model).
- `copier.yml` questions carry `help:` text, derived `default:` expressions (`project_slug` from `project_name`, `package_name` from `project_slug`), and a `validator:` where correctness matters (`package_name.isidentifier()`).
- Docs pages must be registered in the `nav` array in `zensical.toml`; an unlisted `docs/*.md` file will not appear on the site.
