# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> [!NOTE]
> **First-time setup:** This file is boilerplate from the project template.
> If the Project overview below says **TBD**, the project hasn't been initialized yet.
> Read the codebase and `README.md`, then interview the user to learn about the project's purpose, data sources, and specific conventions. Rewrite the TBD sections to reflect the actual project before doing any other work.

## Project overview

**TBD** — interview the user and replace this section.

## Commands

All common tasks are defined in the `justfile`. Run `just` with no arguments to list available targets.

**Install dependencies:**

```bash
uv sync --dev
```

**Format and fix lint issues:**

```bash
just format        # runs ruff format + ruff check --fix
```

**Lint only (no modifications):**

```bash
just lint
```

**Run tests:**

```bash
just test                         # all tests
just test tests/test_submodule.py # single file
just test -k "test_name"          # by name
just pdb                          # drop into IPython debugger on failure
```

**Full QA (format + lint + type-check + tests):**

```bash
just qa
```

**Build docs:**

```bash
just docs          # build to docs/_build/html/
just docs-serve    # live-reload server
```

**Build package:**

```bash
just build
```

## Architecture

### Package layout

```
src/{{ cookiecutter.package_name }}/
├── __init__.py       # exports BASE_DIR, LOG_DIR, DATA_DIR, PLOT_DIR, setup_logger, save
├── cli.py            # Typer-based CLI entry point (registered as `{{ cookiecutter.package_name }}` command)
├── submodule.py      # example submodule
└── core/
    └── utils.py      # setup_logger, save (singledispatch for Figure/DataFrame/Dataset)
```

### Key conventions

**Path variables** — `__init__.py` resolves and exports `BASE_DIR` (project root), `LOG_DIR`, `DATA_DIR`, and `PLOT_DIR` so scripts and notebooks always reference paths relative to the project root rather than their own location.

**`save()` utility** — `core/utils.py` provides a `@functools.singledispatch` `save()` function that dispatches on object type (`plt.Figure` → `savefig`, `pd.DataFrame` → `to_csv`, `xr.Dataset` → `to_netcdf`). The `@add_metadata` decorator automatically appends the git commit hash to filenames and logs provenance.

**CLI** — `cli.py` uses [Typer](https://typer.tiangolo.com/). The app is registered as an entry point in `pyproject.toml` under `[project.scripts]`.

**Environment variables** — `.env` in the project root is loaded automatically at import time via `python-dotenv`. The `LOGLEVEL` variable controls log verbosity (default: `INFO`).

### Testing

Tests live in `tests/` and also run doctests from `src/` (`--doctest-modules` is enabled in `pyproject.toml`). The root `conftest.py` injects `pytest` into the doctest namespace so `pytest.skip()` can be used inside docstring examples.

To skip a doctest example that is only illustrative:

```python
>>> pytest.skip()
>>> # ... illustrative code that should not actually run
```

### Notebooks

Notebooks use [jupytext](https://jupytext.readthedocs.io/) with triple-format pairing (`ipynb` + `py:percent` + `md:myst`). Each notebook should begin with:

```python
%run ../jupyter_startup.ipy
```

This startup script loads autoreload, sets pandas/xarray display options, applies the default matplotlib style from `assets/mpl_styles/`, and makes `BASE_DIR`, `LOG_DIR`, `DATA_DIR`, and `PLOT_DIR` available.

### Linting rules

`ruff.toml` applies to `src/`, `tests/`, and `scripts/`. Docstrings follow the **NumPy convention** (`D` rules with `convention = "numpy"`). Line length is 100. Type annotations are not enforced (`ANN` is intentionally excluded — appropriate for exploratory/research code). See `ruff.toml` for the full list of enabled rule families and the rationale for each exclusion.

### Pre-commit hooks

`.pre-commit-config.yaml` runs `ruff check --fix` then `ruff format` on every commit, and updates `uv.lock` automatically when `pyproject.toml` changes.

### Template updates

This project was generated from a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template and uses [cruft](https://cruft.github.io/cruft/) to pull in upstream template updates. Files listed under `[tool.cruft].skip` in `pyproject.toml` are intentionally excluded from updates.
