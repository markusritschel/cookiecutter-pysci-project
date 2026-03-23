---
icon: material/lightbulb
---

# Tips

## Keep your dependencies up to date with Dependabot

The template ships with a pre-configured [Dependabot](https://docs.github.com/en/code-security/dependabot) setup in `.github/dependabot.yml`. Dependabot automatically opens pull requests to update outdated dependencies on a weekly schedule — it monitors both GitHub Actions versions and uv package dependencies.

To handle these PRs automatically, the template also includes a `dependabot-reviewer` workflow (`.github/workflows/dependabot-reviewer.yml`) that:

- **Auto-approves and merges** patch and minor updates, as well as major updates of development-only dependencies
- **Flags** major updates of production dependencies with a `requires-manual-qa` label for manual review

This means routine maintenance (e.g. bumping `actions/checkout` from v3 to v4) happens without any manual effort.

??? info "Required GitHub settings"

    Two settings must be enabled in your repository before the auto-merge workflow can function:

    1. **Settings → General → Pull Requests → Allow auto-merge** <br />
    Enables the `gh pr merge --auto` command used by the workflow.

    2. **Settings → Actions → General → Workflow permissions → Read and write permissions** <br />
    Allows the `GITHUB_TOKEN` to approve and merge PRs, and to update workflow files when Dependabot bumps GitHub Actions versions.

## Keep your project up to date with cruft

If this template is updated in the future, you can pull in the latest changes to your already-generated project using [cruft](https://cruft.github.io/cruft/):

```bash
uvx cruft update
```

cruft tracks which version of the template your project was generated from and applies only the diff — similar to `git merge` for template updates. Run it periodically to stay current with improvements to the boilerplate.

!!! tip
    If you created your project with `cookiecutter` instead of `cruft`, you can still link it retroactively:
    ```bash
    uvx cruft link https://github.com/markusritschel/cookiecutter-pysci-project
    ```
