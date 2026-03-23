---
icon: simple/pypi
---

# Publishing

Once your package is ready, you can publish it to [PyPI](https://pypi.org/) (Python Package Index) so others can install it with `pip`.

## Prerequisites

1. Create free account at [pypi.org](https://pypi.org/)
2. Generate API token in account settings
3. Add to GitHub repository secrets (for automated publishing)

## Manual Publishing

### 1. Update Version

Edit `pyproject.toml`:

```toml
[project]
name = "your-package"
version = "1.0.0"
description = "Your package description"
```

Follow [Semantic Versioning](https://semver.org/): MAJOR.MINOR.PATCH
- **Major** (1.0.0) - Breaking changes
- **Minor** (0.1.0) - New features
- **Patch** (0.0.1) - Bug fixes

### 2. Update Changelog

Document changes in `CHANGELOG.md`:

```markdown
## Version 1.0.0 (2024-02-25)

### Added
- New feature X

### Fixed
- Bug in module Y
```

### 3. Build Package

```bash
just build
# Creates dist/your-package-*.whl and dist/your-package-*.tar.gz
```

### 4. Upload to PyPI

```bash
just publish
# Equivalent to: uv build && uv publish
```

When prompted for credentials, use:
- Username: `__token__`
- Password: Your PyPI API token

**View on PyPI:**
```
https://pypi.org/project/your-package-name/
```

Users can then install your package:
```bash
pip install your-package-name
```

## Automated Publishing

### 1. Add GitHub Secret

1. Go to **Settings → Secrets and variables → Actions**
2. Create secret named `PYPI_API_TOKEN`
3. Paste your PyPI API token

### 2. Create Workflow

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI
on:
  push:
    tags: ['v*']

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v2
      - run: just build
      - run: |
          uv run twine upload dist/* \
            --username __token__ \
            --password ${{ secrets.PYPI_API_TOKEN }}
```

### 3. Publish by Tag

```bash
just tag    # Creates and pushes tag v1.0.0
# Or manually:
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```
Workflow automatically builds and uploads to PyPI.


!!! note
    Always test your package locally before publishing!
## Configuration Reference

Key `pyproject.toml` fields:

```toml
[project]
name = "package-name"              # Unique on PyPI
version = "1.0.0"
description = "Brief description"
readme = "README.md"
requires-python = ">= 3.10"
license = {file = "LICENSE"}
authors = [{name = "Your Name", email = "you@example.com"}]

[project.urls]
Homepage = "https://github.com/user/package"
Documentation = "https://user.github.io/package"
Repository = "https://github.com/user/package.git"
Issues = "https://github.com/user/package/issues"

[project.scripts]
my-cli = "my_package.cli:main"     # CLI entry point
```

## See Also

- [GitHub Actions](./github-actions.md) - CI/CD workflows
- [Task Automation](./justfile.md) - `just tag` and `just build`

## Further Reading

- [PyPI.org](https://pypi.org/)
- [twine Docs](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)
- [Python Packaging Guide](https://packaging.python.org/)
