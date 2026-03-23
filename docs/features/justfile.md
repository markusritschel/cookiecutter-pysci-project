---
icon: material/console
---

# Task Automation

Similar to `Make`, [Just](https://just.systems/) simplifies the execution of common and repetitive tasks.
This means you can specify targets in your justfile to reduce regularly executed tasks with complex commands (such as building your documentation) from, for example,
```bash
uv run --group docs sphinx-build -b html docs/ docs/_build/html
``` 
to `just docs` :rocket: 

## Task overview
Run `just` in your terminal, and it will list all the recipies available for execution:

```yaml
Available recipes:
  build            # Build the project, useful for checking that packaging is correct
  clean            # Remove all build, test, coverage and Python artifacts
  clean-build      # Remove build artifacts
  clean-docs       # Remove documentation build artifacts
  clean-pyc        # Remove Python file artifacts
  clean-test       # Remove test and coverage artifacts
  coverage         # Run coverage, and build to HTML
  docs             # Compile the documentation
  docs-serve       # Serve the documentation with live reload
  lint *ARGS       # Run ruff check for linting without modifying files
  pdb *ARGS        # Run all the tests, but on failure, drop into the debugger
  publish          # Publish to PyPI (manual alternative to GitHub Actions)
  qa               # Run all the formatting, linting, and testing commands
  tag              # Tag the current version in git and put to github
  test *ARGS       # Run all the tests, but allow for arguments to be passed
  test-gh-actions  # Test github actions locally
  version          # Print the current version of the project
```

Some commands allow for arguments to be passed.
For the exact commands, have a look at the `justfile` code.


## Add your own tasks

You can add custom tasks to your `justfile`, simply by defining a target and the actions to execute:

```bash
deploy:
    #!/usr/bin/env bash
    echo "Deploying..."
    just build
    # Add your deployment commands
```

For more details on Just, read the [Just documentation](https://just.systems/man/en/).
