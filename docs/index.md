---
icon: material/rocket-launch
---

<!-- https://fpgmaas.github.io/cookiecutter-uv/ -->
# PyProject Cookiecutter Template :simple-pythonanywhere:


This is a [CookieCutter](https://www.cookiecutter.io/) template for Python projects.
It uses modern tools for development, testing, and packaging.
Depending on the responses to the [initial prompts](prompts), it can create a boilerplate for data science projects or for a general Python package.

??? note "Requirements"
    To use this template, you need to have [CookieCutter](https://www.cookiecutter.io/) available on your machine.
    Either install it globally via pip or conda, or use `uv` to run it without the need of installing it.
    The latter is recommended.

## Quickstart
To get started, simply run
```bash
uvx cookiecutter gh:markusritschel/cookiecutter-pyproject
```
and follow the [prompts](prompts) to customize your project.
Once finished, navigate into the created directory to start working on your new Python project!

??? note "Without uv"
    If you don't want to use uv, you can also install CookieCutter globally and run it with the following command:
    ```bash
    cookiecutter gh:markusritschel/cookiecutter-pyproject
    ```


## Features

This template comes ready with a collection of modern and useful tools for an efficient [development flow](features/development.md):

- **[Package Management](features/uv.md)**: [uv](https://docs.astral.sh/uv/) for blazingly fast dependency management and virtual environments (it's _a lot_ faster than conda 🚀)
- **[Code Quality](features/code-quality.md)**: Ruff for linting & formatting, ty for type checking, pytest for testing
- **[Task Automation](features/justfile.md)**: Just as a modern Make alternative (`just qa`, `just docs`, …)
- **[GitHub Actions CI/CD](features/github-actions.md)**: Automated testing, linting, and documentation deployment; Dependabot for dependency updates
- **[Documentation](features/documentation.md)**: Sphinx with MyST Markdown, autoapi, and GitHub Pages deployment
- **[Publishing](features/publish-package.md)**: PyPI publishing via `just publish` or automated GitHub Actions workflow
- **[Research Projects](features/research-projects.md)**: Optional data science structure: `data/`, `notebooks/`, `reports/`
- **src layout**: Ensures tests always run against the installed package, not loose source files
- **DevContainer**: VSCode dev container for a reproducible development environment


## How to continue

Read the [Tutorial](./tutorial) for a step-by-step guide to create a new project.
In the features section you can find detailed documentation for each tool and feature (links above).
