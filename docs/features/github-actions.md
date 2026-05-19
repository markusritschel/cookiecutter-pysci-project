---
icon: fontawesome/brands/github
---

# GitHub Actions CI/CD

The template includes automated Continuous Integration (CI) and Continuous Deployment (CD) via [GitHub Actions](https://github.com/features/actions).

!!! NOTE
    Keep in mind that the deployment may take a while. You can check the status of the workflow by clicking on "Action" in the menu bar of your repository.

## Workflow Files

The template uses two separate workflow files:

### `main.yml` — CI

Runs on every push to `main` or `develop`, and on pull requests targeting `main`.

**`build` job** (matrix: Python 3.10, 3.12):

1. **Setup**: Installs uv and syncs all dev dependencies (`uv sync --locked --dev`)
2. **Format check & lint**: Runs `ruff format --check` followed by `ruff check` — both must pass; no auto-fixing
3. **Testing**: Runs `pytest -v`
4. **Coverage**: Uploads coverage data to [Codecov](https://codecov.io/) (requires `CODECOV_TOKEN` secret)

### `docs.yml` — Documentation

Runs only on pushes to `main` when documentation-related files change (`docs/**`, `src/**`, `*.md`). Can also be triggered manually via the GitHub Actions UI (`workflow_dispatch`).

**`build-documentation` job**: Installs Pandoc and builds Sphinx docs

**`deploy-documentation` job** (runs after `build-documentation`): Deploys built docs to GitHub Pages


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
