---
icon: fontawesome/brands/github
---

# GitHub Actions CI/CD

The template includes automated Continuous Integration (CI) and Continuous Deployment (CD) via [GitHub Actions](https://github.com/features/actions).

## Workflow File

The main workflow is defined in `.github/workflows/main.yml`. It automatically runs on:

- **Push to `main` or `develop`** branches
- **Pull requests** targeting the `main` branch

## What the Workflow Does

The CI/CD pipeline is split into three jobs:

**`build` job** (matrix: Python 3.10, 3.12):

1. **Setup**: Installs uv and syncs all dev dependencies
2. **Linting**: Runs `ruff check` twice: once for critical errors (syntax/undefined names), once for the full rule set with `--exit-zero` (warnings only)
3. **Testing**: Runs `pytest -v`
4. **Coverage**: Uploads coverage data to [Codecov](https://codecov.io/) (requires `CODECOV_TOKEN` secret)

**`build-documentation` job** (runs after `build`): <br />
Installs Pandoc and builds Sphinx docs

**`deploy-documentation` job** (runs after `build-documentation`, main branch only): <br />
Deploys built docs to GitHub Pages

## Workflow Status

Pull requests show status checks:

- ✅ **Passed** - All checks successful; safe to merge
- ❌ **Failed** - Fix issues before merging
- ⏳ **Running** - Workflow in progress


## Enable GitHub Pages Deployment

1. Go to **Settings → Pages**
2. Set source to **GitHub Actions**
3. Docs deploy automatically on main branch commits (URL: `https://<username>.github.io/<repo>`)


## Troubleshooting

**Workflow failed** – Click the run to view logs and find the failing step.

**Docs didn't deploy** – Verify GitHub Pages is set to use GitHub Actions as the source.

**Codecov upload skipped** – Add `CODECOV_TOKEN` to your repository secrets (**Settings → Secrets and variables → Actions**).

## See Also

- [Publishing](./publish-package.md) - PyPI deployment
- [Documentation](./documentation.md) - What gets built

## Further Reading

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [uv GitHub Actions Setup](https://github.com/astral-sh/setup-uv)
