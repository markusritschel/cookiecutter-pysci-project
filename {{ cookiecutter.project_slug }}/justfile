# See https://just.systems/ for more information

# Show available commands
list:
    @just --list

# Run ruff check for linting without modifying files
lint *ARGS:
    uv run --group test ruff check {{ARGS}}

# Run all the formatting, linting, and testing commands
qa:
    uv run --group test ruff format .
    uv run --group test ruff check . --fix
    uv run --group test ruff check --select I --fix .
    uv run --group test ty check .
    uv run --group test pytest .

# Run all the tests, but allow for arguments to be passed
test *ARGS:
    @echo "Running with arg: {{ARGS}}"
    uv run --group test pytest {{ARGS}}

# Run all the tests, but on failure, drop into the debugger
pdb *ARGS:
    @echo "Running with arg: {{ARGS}}"
    uv run  --group test pytest --pdb --maxfail=10 --pdbcls=IPython.terminal.debugger:TerminalPdb {{ARGS}}

# Run coverage, and build to HTML
coverage:
    uv run --group test coverage run -m pytest .
    uv run --group test coverage report -m
    uv run --group test coverage html

# Build the project, useful for checking that packaging is correct
build:
    rm -rf build
    rm -rf dist
    uv build

VERSION := `grep -m1 '^version' pyproject.toml | sed -E 's/version = "(.*)"/\1/'`

# Print the current version of the project
version:
    @echo "Current version is {{VERSION}}"

# Compile the documentation
docs:
    uv run --group docs sphinx-build -b html docs/ docs/_build/html

# Serve the documentation with live reload
docs-serve:
    uv run --group docs sphinx-autobuild --open-browser docs/ docs/_build/html

# Tag the current version in git and put to github
tag:
    @echo "Tagging version v{{VERSION}}"
    git tag -a v{{VERSION}} -m "Creating version v{{VERSION}}"
    git push origin v{{VERSION}}

# Remove all build, test, coverage and Python artifacts
clean: clean-build clean-docs clean-pyc clean-test

# Remove build artifacts
clean-build:
    @echo "Cleaning build artifacts..."
    @rm -fr build/ dist/ .eggs/
    @find . -name '*.egg-info' -exec rm -fr {} +
    @find . -name '*.egg' -exec rm -f {} +

# Remove documentation build artifacts
clean-docs:
    @echo "Cleaning documentation build artifacts..."
    @rm -fr docs/_build/ docs/api/

# Remove Python file artifacts
clean-pyc:
    @echo "Cleaning Python file artifacts..."
    @find . -name '*.pyc' -exec rm -f {} +
    @find . -name '*.pyo' -exec rm -f {} +
    @find . -name '*~' -exec rm -f {} +
    @find . -name '__pycache__' -exec rm -fr {} +

# Remove test and coverage artifacts
clean-test:
    @echo "Cleaning test and coverage artifacts..."
    @rm -f .coverage
    @rm -fr htmlcov/ .pytest_cache

# Test github actions locally
test-gh-actions:
	@mkdir -p /tmp/artifacts
	act push --artifact-server-path /tmp/artifacts --container-options "--userns host" --action-offline-mode

# Publish to PyPI (manual alternative to GitHub Actions)
publish:
    uv build
    uv publish
