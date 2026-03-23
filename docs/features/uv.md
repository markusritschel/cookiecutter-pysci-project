---
icon: material/package-variant-closed
---

# Package Management

[uv](https://docs.astral.sh/uv/) is a fast Python package installer and virtual environment manager that replaces traditional tools like `pip`, `pip-tools`, and `venv`. The template uses uv as the primary tool for dependency management.

## Virtual Environment

uv automatically creates and manages virtual environments. When you run commands with `uv`, it creates a `.venv` directory if one doesn't exist:

=== "macOS/Linux"
    ```bash
    # Initialize and activate the virtual environment
    uv venv
    source .venv/bin/activate
    ```

=== "Windows"
    ```powershell
    # Initialize and activate the virtual environment
    uv venv
    .\.venv\Scripts\activate
    ```

## Managing Dependencies

The template defines dependencies in `pyproject.toml` with organized dependency groups:

```toml title="pyproject.toml"
[project]
dependencies = [
  "click",
  "colorama",
  "pandas",
  "numpy",
]

[dependency-groups]
dev = [
  {include-group = "lint"},
  {include-group = "test"}
]
lint = [
  "ruff",
  "ty",
]
test = [
  "pytest",
  "pytest-cov"
]
docs = [
  "sphinx",
  "sphinx-autoapi",
  "myst-parser"
]
```

## Common uv Commands

**Sync dependencies** - Install all project dependencies:
```bash
uv sync
uv sync --group dev  # Include development dependencies
```

**Add a package** - Add a new dependency to the project:
```bash
uv add requests
uv add --group dev pytest-xdist
```

**Run commands** - Execute Python or installed tools within the virtual environment:
```bash
uv run python script.py
uv run --group dev pytest
uv run --group docs sphinx-build -b html docs/ docs/_build/html
```

**Build the project** - Create distributable packages:
```bash
uv build
```

## Dependency Resolution

uv automatically resolves dependency conflicts and creates a `uv.lock` file that pins exact versions for reproducible builds. This lock file should be committed to version control to ensure all team members use identical dependency versions.

## Integration with Tasks

The template's `justfile` tasks use `uv run` with specific dependency groups:

- `just lint` - Runs `ruff check` via the `test` group
- `just test` - Runs `pytest` via the `test` group
- `just qa` - Runs format, lint, type check, and tests via the `test` group
- `just docs` - Builds Sphinx docs via the `docs` group

See [Task Automation with Just](./justfile.md) for complete task documentation.

## Further Reading

- [uv Documentation](https://docs.astral.sh/uv/)
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 508 - Dependency Specification](https://www.python.org/dev/peps/pep-0508/)
