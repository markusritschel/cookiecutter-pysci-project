---
icon: material/code-braces
---

# Development Flow

This template provides a full, modern development environment with integrated tools for testing, code quality, and documentation.


## Core Tools

| Tool       | Purpose                                     |
| ---------- | ------------------------------------------- |
| **uv**     | [Dependency & environment manager](./uv.md) |
| **Ruff**   | [Linting & formatting](./code-quality.md)   |
| **ty**     | [Type checking](./code-quality.md)          |
| **pytest** | [Testing & coverage](./code-quality.md)     |
| **Just**   | [Task automation](./justfile.md)            |
| **Sphinx** | [Documentation](./documentation.md)         |


## Getting Started

I recommend you to use `uv` as a dependency and environment manager.
Read the corresponding section of the documentation [here](./uv).
In your project's directory, run the following commands 

=== "macOS/Linux"
    ```bash
    uv venv

    source .venv/bin/activate

    uv sync --dev
    just qa                    # Verify setup
    ```

=== "Windows"
    ```powershell
    uv venv

    .\.venv\Scripts\activate

    uv sync --dev
    just qa                    # Verify setup
    ```

To get more familiar with `uv`, I recommend you to have a look at [their documentation](https://docs.astral.sh/uv/).

***

## A typical Development Workflow

### 1. Write Code

Edit source code in `src/mypackage/`:

```python
def user_data(name: str, age: int) -> dict: # (1)!
    """Process user data.
    
    Parameters
    ----------
    name : str
        User's full name
    age : int
        User's age in years
    """ # (2)!
    return {name: age}
```

1. Always make use of type hints
2. Give your functions meaningful docstrings, including parameter information and (if it helps the understanding) examples.

### 2. Write Tests

Add tests in `tests/`:

```python
def test_user_data():
    assert user_data("Albert", 30) == {"Albert": 30}
```

### 3. Run Quality Checks

```bash
just qa            # Format → Lint → Type check → Test
```

### 4. Commit

```bash
git add .
git commit -m "Add user_data function"
```
!!! tip "Best practice"
    Make atomic commits. That is, commit every logical "bite" that does something meaningful in your code.
    Use "active" language, i.e. describe what the commit does when applied.


### 5. Update Documentation

Keep your project's [documentation](./documentation) up-to-date. Edit the markdown files in `docs/` and preview the rendered version, running
```bash
just docs-serve    # View at http://localhost:8000
```


### 6. Push to Github
```bash
git push
```

GitHub Actions automatically runs CI/CD. See [GitHub Actions](./github-actions.md). <br />
If GitHub pages is configured, your documentation will be served online on `https://<your-username>.github.io/<package-slug>`.


*** 

## Common Tasks

| Task               | Command                       |
| ------------------ | ----------------------------- |
| Add dependency     | `uv add package-name`         |
| Add dev dependency | `uv add --group dev package`  |
| Run specific test  | `just test tests/test_foo.py` |
| Format code        | `uv run ruff format .`        |
| Type check         | `uv run ty check .`           |
| Build package      | `just build`                  |
| Clean artifacts    | `just clean`                  |


## Project Structure

The `src/` layout ensures tests run against installed package.

```yaml
├── src/mypackage/
├── tests/
├── docs/
├── notebooks/      # Jupyter notebooks for data exploration (1)
├── reports/        # Data reports, figures, etc. (2)
├── pyproject.toml  # (3)!
├── ruff.toml
└── justfile  # (4)!
```

1. Only present if `is_research_project` is answered with `yes`
2. Only present if `is_research_project` is answered with `yes`
3. Most of the project's configuration is in here
4. The justfile holds default tasks that can run simply like `just docs`.


## See Also

- [Code Quality](./code-quality.md) - Linting, type checking, testing
- [Task Automation](./justfile.md) - Available tasks
- [Documentation](./documentation.md) - Building docs
- [GitHub Actions](./github-actions.md) - CI/CD pipeline

## Further Reading

- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Docs](https://pytest.org/)
- [Sphinx Docs](https://www.sphinx-doc.org/)



