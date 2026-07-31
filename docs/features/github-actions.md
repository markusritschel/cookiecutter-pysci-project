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

Runs on every push to `main` or `develop`, on pull requests targeting `main`, and on demand via the GitHub Actions UI (`workflow_dispatch`).

**`build` job** (matrix: Python 3.10, 3.12):

1. **Setup**: Installs uv and syncs all dev dependencies (`uv sync --locked --dev`)
2. **Lint**: Runs `ruff check . --output-format=github`, so violations appear as inline annotations on the diff
3. **Format check**: Runs `ruff format --check .` — no auto-fixing[^ci-format]
4. **Testing**: Runs `pytest -v`
5. **Coverage**: Uploads coverage data to [Codecov](https://codecov.io/) (requires `CODECOV_TOKEN` secret)
6. **Labeling**: Applies labels via [`actions/labeler`](https://github.com/actions/labeler) according to the rules in `.github/labeler.yml`

[^ci-format]: Formatting is deliberately kept out of CI's control: it should be applied locally
    (`just format`, or the pre-commit hook) rather than committed back by a workflow.

### `docs.yml` — Documentation

Runs only on pushes to `main` when documentation-related files change (`docs/**`, `src/**`, `*.md`). Can also be triggered manually via the GitHub Actions UI (`workflow_dispatch`).

**`build-documentation` job**: Installs uv, syncs the `docs` dependency group, and builds the documentation with the engine you chose during generation. The workflow is generated to match that choice — Sphinx and MyST additionally get Pandoc installed, and the artifact is uploaded from `docs/_build/html/` for Sphinx and MyST, or from `site/` for Zensical.

**`deploy-documentation` job** (runs after `build-documentation`): Deploys the uploaded artifact to GitHub Pages


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
