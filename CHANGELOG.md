# Change Log

## Unreleased

- **Fixed:** the example/boilerplate files (`submodule.py`, `docs/example.md`, the demo notebook, everything in `tests/`) were missing from *every* generated project, and `cli.py` was emitted as a CLI app with no commands behind a registered entry point. They had been guarded with `{% if _copier_operation == 'copy' %}` — in the filename for the former, around the body for the latter — but copier only defines `_copier_operation` when evaluating `_tasks`/`_migrations` conditions; during path and content rendering it is undefined, so the condition was always false, filenames rendered to an empty stem and the guarded body rendered empty. Intent is now expressed via `_skip_if_exists`, which does not resurrect files the user deleted because `copier update` applies a template-side diff. Added `tests/` at the repo root, which renders the template and asserts on the generated tree, and wired the template's own tests into CI — the existing pipeline could not catch this, since `pytest` in a generated project exits 0 on the `src/` doctests even with an empty `tests/`
- The `command_line_interface` question now has an effect. Previously all four answers produced the same Typer `cli.py`, entry point and dependency set; now each generates the matching CLI and only the selected library, and "No command-line interface" omits `cli.py` and `[project.scripts]` altogether
- The `command_line_interface` question now defaults to "No command-line interface" (previously Typer) — choose Typer, Click or Docopt to opt in
- Removed the `Makefile` and consolidated on `just`. It predated the uv migration and contradicted the justfile beside it (conda environments, an editable install via pip, a hardcoded `sphinx-build` regardless of the chosen docs engine, and the invalid flag `uv sync --groups docs`). Its figure-processing targets — the only content `just` did not already cover — were ported to the justfile for research projects; keeping a second task runner just for those was rejected. Since this makes `just` a de-facto requirement, the generated `README.md` gained a "Don't have `just`?" section giving the plain `uv` command behind each common recipe (every recipe is a thin wrapper around one), the docs now cover installing it via `uv tool install rust-just`, and the repository README no longer calls `just` "optional but recommended"
- Rewrote the generated `README.md` around uv and just. It still instructed users to run `make conda-env`, `make src-available` and `make documentation` and recommended Conda/Mamba, contradicting the generated docs, which already documented `uv sync`. Its structure listing advertised `setup.py`, `requirements.txt`, `environment.yml`, `src/tests` and `reports/book`, none of which the template produces
- Fixed `pytest` `addopts` passing `"-ra -v"` as one entry, which argparse read as `-r` with the value `"a -v"`, silently dropping `-v`
- Fixed ruff `target-version = "py311"` against `requires-python = ">=3.10"`, which let the `UP` rules rewrite to syntax the lowest supported (and CI-tested) interpreter cannot parse
- Fixed the generated docs workflow referencing `steps.deployment.outputs.page_url` with no step carrying `id: deployment`, which left the GitHub Pages environment URL empty
- Fixed the package `__init__.py` appending a `scripts/` path that only exists for research projects, and importing `sys` solely for it, which tripped ruff F401 on library projects
- Replaced the example notebook's kernelspec, which was pinned to a personal conda environment
- Removed duplicate and unusable runtime dependencies (`jupytext` listed twice; `jupyterbook-latex` and `mystmd` in both the main dependencies and the docs group; `nodejs` and `pandoc`, which are not usable as PyPI packages)
- Renamed copier questions to copier's well-known variable names: `project_author` → `user_name`, `email` → `user_email`, `github_username` → `github_user`. Projects generated under the old names are remapped automatically on `copier update` via a `_migrations` entry in `copier.yml`.
- Added `scripts/migrate_cookiecutter_to_copier.py` to bootstrap a `.copier-answers.yml` for projects still generated with the old cookiecutter/cruft template, so they can adopt `copier update` — see [docs/tips.md](docs/tips.md#migrating-an-existing-cookiecuttercruft-project-to-copier)
- Project generation now uses `uvx --with jinja2-time copier copy gh:markusritschel/cookiecutter-pyproject my-project`
- Template updates now use `copier update` (replacing `cruft update`), tracked via the generated `.copier-answers.yml`
- Removed `cookiecutter.json` and the `hooks/` directory; prompts, conditional generation, and post-generation setup are now defined in `copier.yml`
- Replaced the inline POSIX-shell post-generation `_tasks` (git init/commit, `uv sync --dev`, pre-commit install) with a standalone `tasks/post_gen.py`, so project generation also works on native Windows without WSL/git-bash; the simpler inline-shell approach was considered but rejected for not being cross-platform
- Updated all user-facing documentation (README, docs site) to the copier workflow
- Migrated the template engine from cookiecutter (+ cruft for updates) to [copier](https://copier.readthedocs.io) — rationale in [docs/tips.md](docs/tips.md#why-copier-instead-of-cookiecutter-and-cruft)

## 1.0.0

- Merged two repositories ([cookiecutter-pypackage](https://github.com/markusritschel/cookiecutter-pypackage) & [cookiecutter-pysci-project](https://github.com/markusritschel/cookiecutter-pysci-project))
- Renamed the repository to `cookiecutter-pyproject`
- The new project now has its own documentation hosted on GitHub pages
- The documentation now includes more detailed information in favour of a shortened README.md
- Now uses `uv` as dependency manager
- Now uses justfile as taskrunner
- Now has extensive documentation on https://markusritschel.github.io/cookiecutter-pyproject/
- Uses Zensical for main documentation
