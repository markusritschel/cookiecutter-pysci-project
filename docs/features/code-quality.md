---
icon: material/shield-check
---

# Code Quality

This template includes modern tools to ensure consistent, high-quality code through automated linting, formatting, type checking, and testing.

## Linting & Formatting with Ruff

[Ruff](https://docs.astral.sh/ruff/) is an extremely fast Python linter and code formatter written in Rust. It replaces multiple tools (flake8, isort, black) with a single, unified tool.

**Configuration** in `ruff.toml`:

```toml title="ruff.toml"
line-length = 88
indent-width = 4

[format]
quote-style = "double"
indent-style = "space"

[lint]
select = [
    "D",    # pydocstyle - documentation standards
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # Pyflakes - logical errors
    "I",    # isort - import sorting
    "B",    # flake8-bugbear - common bugs
    "UP",   # pyupgrade - Python syntax upgrades
    "C901", # mccabe complexity detection
]

[lint.pydocstyle]
convention = "numpy"  # Or "google", "sphinx", etc.  # (1)!
```

1. Choose one out of `{numpy,google, pep257}`. See also [Docstring Conventions](#docstring-conventions).

**Commands:**

| Task                     | Command                                |
| ------------------------ | -------------------------------------- |
| Check code w/o modifying | `uv run ruff check .`                  |
| Auto-fix violations      | `uv run ruff check . --fix`            |
| Format code              | `uv run ruff format .`                 |
| Sort imports             | `uv run ruff check --select I --fix .` |

Also check out the justfile shortcuts `just lint` and `just qa`.


## Type Checking with ty

[ty](https://docs.astral.sh/ty/) is a fast static type checker from the Ruff creators. It validates type annotations without running code.
Type hints help catch errors early and improve code clarity[^type-hints].

[^type-hints]: See [Python Type Hints](https://docs.python.org/3/library/typing.html) for syntax.

```python
def process_data(name: str, age: int) -> dict:
    """Process user data.
    
    Parameters
    ----------
    name : str
        User's full name
    age : int
        User's age in years
    """
    return {name: age}
```

**Commands:**

| Task                     | Command                                   |
| ------------------------ | ----------------------------------------- |
| Type check codebase      | `uv run ty check .`                       |
| Type check specific file | `uv run ty check src/mypackage/module.py` |

!!! info "Type checking in IDE"
    - `ty` provides a language server for real-time type checking
    - Most editors (VSCode, PyCharm) integrate with `ty` automatically


## Testing with pytest

[pytest](https://pytest.org/) runs unit tests and validates code behavior. Tests ensure your code works as expected and catch regressions.

**Configuration** in `pyproject.toml`:

```toml title="pyproject.toml"
[tool.pytest.ini_options]
minversion = "6.0"
testpaths = ["tests", "src"] # (1)!
addopts = [
    "--doctest-modules",
    "--doctest-continue-on-failure",
    "-ra -v",
    "--cov=./src",
    "--cov-report=xml",
    "--cov-report=html",
    "--cov-report=term-missing"
]
```

1. These are the paths where `pytest` will search for tests.



**Commands:**

| Task                         | Command                                                  |
| ---------------------------- | -------------------------------------------------------- |
| Run all tests                | `uv run pytest .` or `just test`                         |
| Run specific test file       | `uv run pytest tests/test_module.py`                     |
| Run specific test            | `uv run pytest tests/test_module.py::test_function_name` |
| Run tests matching pattern   | `uv run pytest -k "test_helper"`                         |
| Run with debugger on failure | `just pdb`[^pytest-debug]                                |
| Generate coverage report     | `just coverage`[^pytest-cov]                             |

[^pytest-debug]: Drops into IPython debugger when test fails, allowing inspection.

[^pytest-cov]: Generates a Terminal report showing % coverage per file as well as an HTML report in `htmlcov/index.html`.

!!! tip "Tip: Aim for >80% coverage"
    Focus on testing:

    - all public functions
    - edge cases and error conditions
    - critical code paths


## Running All Quality Checks

Execute all checks at once:

```bash
just qa
```

Runs in order: formatting → linting → import sorting → type checking → tests

!!! tip
    Use this before committing code.


## Project Structure

The template uses a `src/` layout, ensuring that tests run against the installed package:

```
project/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── module.py
├── tests/
│   ├── conftest.py
│   └── test_module.py
├── pyproject.toml
└── ruff.toml
```

This way, tests validate distribution, not local files.
They also catch missing dependencies or import issues.


## Integration with CI/CD

GitHub Actions runs Ruff ynd pytest automatically on every push and pull request. 
All checks must pass before merging. 
See [GitHub Actions CI/CD](./github-actions.md).


## Configuration Best Practices

### Docstring Conventions

Choose one standard for your project and configure Ruff accordingly:

```toml title="ruff.toml"
[lint.pydocstyle]
convention = "numpy"
```

- **NumPy** - for comprehensive, scientific projects
- **Google** - for simple, readable format
- **PEP257** - Python fall-back convention

See also the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#google-vs-numpy) and [Ruff settings](https://docs.astral.sh/ruff/settings/#lint_pydoclint_ignore-one-line-docstrings).

### Strict Type Checking

Add to `pyproject.toml` for stricter type checking:

```toml
[tool.ty]
python_version = "3.10"
strict = true  # Requires full type annotations
```

## Further Reading

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Ruff Rules Reference](https://docs.astral.sh/ruff/rules/)
- [ty Documentation](https://docs.astral.sh/ty/)
- [pytest Documentation](https://pytest.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
