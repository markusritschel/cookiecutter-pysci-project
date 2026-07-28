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

## Keep your project up to date with copier

If this template is updated in the future, you can pull in the latest changes to your already-generated project using [copier](https://copier.readthedocs.io). Run this from inside your project directory:

```bash
uvx --with jinja2-time copier update --trust
```

copier records the template version your project was generated from in the `.copier-answers.yml` file and applies only the diff — similar to `git merge` for template updates. Run it periodically to stay current with improvements to the boilerplate. Commit (or stash) any local changes first; copier refuses to update a dirty working tree.

!!! tip "The answers file"
    The `.copier-answers.yml` file at the root of your project stores the answers you gave to the [prompts](prompts.md) and the template version you generated from. Keep it under version control — copier reads it to reuse your answers and to compute the update diff. Editing it by hand is rarely necessary, but you can adjust an answer there before running `copier update`.

## Migrating an existing cookiecutter/cruft project to copier

If your project was generated before the template moved to copier, it has a `.cruft.json` instead of a `.copier-answers.yml` and can't run `copier update` yet. [`scripts/migrate_cookiecutter_to_copier.py`](https://github.com/markusritschel/cookiecutter-pyproject/blob/main/scripts/migrate_cookiecutter_to_copier.py) bootstraps the answers file for you: it reads your project's `.cruft.json`, maps the old cookiecutter keys onto the current copier question keys (`project_author` → `user_name`, `email` → `user_email`, `github_username` → `github_user`), and writes `.copier-answers.yml`. It does not touch any other file.

Run it from a checkout of this template, pointed at your project:

```bash
uv run scripts/migrate_cookiecutter_to_copier.py /path/to/your-project
```

Then commit the new `.copier-answers.yml` and run `copier update --trust` in your project as usual.

!!! note "No `.cruft.json`?"
    If your project was generated with plain `cookiecutter` rather than `cruft`, it won't have a `.cruft.json` and the script will exit with an error telling you so. Create one first by linking the project to this template — this only records the template's current state, it doesn't touch any files:
    ```bash
    cd /path/to/your-project
    uvx cruft link https://github.com/markusritschel/cookiecutter-pyproject
    ```
    Then re-run the migration script as above.

!!! warning "Known limitation"
    The script only bootstraps the answers file — it can't know about template files you've since deleted or heavily rewritten (e.g. example tests, placeholder docs). The first `copier update` may recreate a small number of such files; review the diff and remove anything you don't want, same as any other update.

!!! info "Why `LICENSE` and `CITATION.cff` don't get rewritten on update"
    The template stamps the copyright year in `LICENSE` and the `date-released` field in `CITATION.cff` using Jinja's `{% now %}` (via `jinja2_time`), which re-evaluates every time it runs. Without protection, a routine `copier update` would silently overwrite both dates with today's date. Both files are listed in `copier.yml`'s `_skip_if_exists`, the same mechanism already used for `README.md` and other user-owned files, so once they exist in your project `copier update` leaves them untouched. An earlier proposal replaced `jinja2_time` with a placeholder-and-post-gen-script convention instead; it was rejected because the actual scope — two known files — didn't justify a parallel mechanism when `_skip_if_exists` already solves exactly this problem. The tradeoff: `_skip_if_exists` freezes the whole file, so future structural changes to these templates won't propagate to already-generated projects either — acceptable here since neither file is expected to need auto-updates.

## A note on version controlling Jupyter notebooks

It is very ugly to keep Jupyter Notebooks under version control as they are in principle a very large JSON file, containing lots of metadata, output of your cells, etc.
This circumstance makes it also quite hard to collaborate on them. 

However, there's help: *[Jupytext](https://jupytext.readthedocs.io/)* syncs your Jupyter notebooks with another file for which you can choose a variety of formats (e.g. Markdown, R Markdown, normal Python, etc.).
These "paired" files, which can either reside alongside your Jupyter notebooks or in a separate directory, can then be easily version-controlled.
*Jupytext* can either be used from the command line (`jupytext --sync notebooks/*ipynb`) or as a Jupyter plugin.

For more information, visit https://jupytext.readthedocs.io/.
