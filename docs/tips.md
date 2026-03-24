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
    uvx cruft link https://github.com/markusritschel/cookiecutter-pyproject
    ```


## A note on version controlling Jupyter notebooks

It is very ugly to keep Jupyter Notebooks under version control as they are in principle a very large JSON file, containing lots of metadata, output of your cells, etc.
This circumstance makes it also quite hard to collaborate on them. 

However, there's help: *[Jupytext](https://jupytext.readthedocs.io/)* syncs your Jupyter notebooks with another file for which you can choose a variety of formats (e.g. Markdown, R Markdown, normal Python, etc.).
These "paired" files, which can either reside alongside your Jupyter notebooks or in a separate directory, can then be easily version-controlled.
*Jupytext* can either be used from the command line (`jupytext --sync notebooks/*ipynb`) or as a Jupyter plugin.

For more information, visit https://jupytext.readthedocs.io/.
