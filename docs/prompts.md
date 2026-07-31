---
icon: material/form-textbox
---

# Prompts

When creating your project from this template, copier will ask you a series of questions.
Your answers are recorded in a `.copier-answers.yml` file in the generated project, so they can be reused when you later run `copier update` (see [Tips](tips.md)).
All answers can be changed afterward, but `package_name` in particular occurs in multiple places (including directory names), so choose it carefully upfront.

## Personal information

**`user_name`**
<br />   Your full name. Used in documentation and project metadata.

**`user_email`**
<br />   Your e-mail address. Used for metadata and `pyproject.toml`.

**`github_user`**
<br />   Your GitHub username. Used to generate repository links.

## Project naming

**`project_name`**
<br />   A concise, human-readable project name (may include spaces and capitals, e.g. `"My New Project"`).

**`project_slug`** *(auto-derived)*
<br />   URL-friendly version of `project_name` — spaces replaced by dashes, lowercased.
    Becomes the repository name and top-level directory.

**`package_name`** *(auto-derived)*
<br />   Python import name derived from `project_slug` — dashes replaced by underscores.
    Used in `import` statements, so it must be a valid Python identifier.

## Project setup

**`is_research_project`** *(default: `true`)*
<br />   When `true`, the project includes directories for data science workflows:
    `data/`, `notebooks/`, `reports/`, `scripts/`, `references/`.
    Set to `false` for a plain Python package without those extras.

**`project_description`**
<br />   A one-line description of your project. Used in `pyproject.toml`, README, and docs.

**`project_version`** *(default: `0.1.0`)*
<br />   Initial version following [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

## Tool choices

**`command_line_interface`** *(default: `No command-line interface`)*
<br />   Scaffolds `src/<package>/cli.py` and a `[project.scripts]` entry point using the selected
    framework. All three flavours expose the entry point as `app`. See [Command-Line
    Interface](features/cli.md).

| Choice   | Description                          |
| -------- | ------------------------------------ |
| `Typer`  | Modern, type-hint-based CLI          |
| `Click`  | Decorator-based, widely used         |
| `Docopt` | Docstring-driven argument parsing    |
| `No command-line interface` | No `cli.py` and no entry point (default) |

**`project_license`**
<br />   The license to include. Choices: `MIT`, `BSD`, `ISC`, `Apache 2.0`, `GPL v3`, `Not open source`.

**`docs_engine`** *(default: `Sphinx`)*
<br />   Documentation toolchain to set up. This determines the contents of `docs/`, the `docs`
    dependency group, the commands behind `just docs`, and the generated documentation workflow —
    see [Documentation](features/documentation.md) for a full comparison.

| Choice    | Description                                                                 |
| --------- | --------------------------------------------------------------------------- |
| `Sphinx`  | Classic Python docs, written in Markdown via MyST. The only option with API docs generated from your docstrings, and the right default for a package |
| `Zensical`| Successor to Material for MkDocs. Fastest builds and the most polished default site; no API docs and no BibTeX |
| `MyST`    | [MyST-MD](https://mystmd.org/), a separate Markdown-first toolchain for scientific writing (*not* a Sphinx variant). Native citations, no API docs |
