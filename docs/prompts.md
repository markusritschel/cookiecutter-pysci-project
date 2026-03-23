---
icon: material/form-textbox
---

# Prompts

When creating your project from this template, CookieCutter will ask you a series of questions.
All answers can be changed afterward, but `package_name` in particular occurs in multiple places (including directory names), so choose it carefully upfront.

## Personal information

**`project_author`**
<br />   Your full name. Used in documentation and project metadata.

**`email`**
<br />   Your e-mail address. Used for metadata and `pyproject.toml`.

**`github_username`**
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

**`command_line_interface`**
<br />   Scaffolds a CLI module in your package using the selected framework:

| Choice   | Description                          |
| -------- | ------------------------------------ |
| `Typer`  | Modern, type-hint-based CLI          |
| `Click`  | Decorator-based, widely used         |
| `Docopt` | Docstring-driven argument parsing    |
| `None`   | No CLI module generated              |

**`project_license`**
<br />   The license to include. Choices: `MIT`, `BSD`, `ISC`, `Apache 2.0`, `GPL v3`, `Not open source`.

**`docs_engine`**
<br />   Documentation toolchain to set up:

| Choice    | Description                                  |
| --------- | -------------------------------------------- |
| `Sphinx`  | Classic Python docs with MyST Markdown       |
| `Zensical`| MkDocs Material-based, modern look           |
| `MyST`    | Lightweight Markdown-first Sphinx variant    |
