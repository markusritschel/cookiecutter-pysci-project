# Change Log

## Unreleased

- Renamed copier questions to copier's well-known variable names: `project_author` → `user_name`, `email` → `user_email`, `github_username` → `github_user`. Projects generated under the old names are remapped automatically on `copier update` via a `_migrations` entry in `copier.yml`.
- Added `scripts/migrate_cookiecutter_to_copier.py` to bootstrap a `.copier-answers.yml` for projects still generated with the old cookiecutter/cruft template, so they can adopt `copier update` — see [docs/tips.md](docs/tips.md#migrating-an-existing-cookiecuttercruft-project-to-copier)
- Project generation now uses `uvx --with jinja2-time copier copy gh:markusritschel/cookiecutter-pyproject my-project`
- Template updates now use `copier update` (replacing `cruft update`), tracked via the generated `.copier-answers.yml`
- Removed `cookiecutter.json` and the `hooks/` directory; prompts, conditional generation, and post-generation setup are now defined in `copier.yml`
- Replaced the inline POSIX-shell post-generation `_tasks` (git init/commit, `uv sync --dev`, pre-commit install) with a standalone `tasks/post_gen.py`, so project generation also works on native Windows without WSL/git-bash; the simpler inline-shell approach was considered but rejected for not being cross-platform
- Updated all user-facing documentation (README, docs site) to the copier workflow
- Migrated the template engine from cookiecutter (+ cruft for updates) to [copier](https://copier.readthedocs.io) — rationale in [docs/tips.md](docs/tips.md#why-copier-instead-of-cookiecutter-and-cruft)

## 1.0.0

- Merged two repositories ([cookiecutter-pypackage](https://github.com/markusritschel/cookiecutter-pypackage) & [cookiecutter-pysci-project](https://github.com/markusritschel/cookiecutter-pysci-project))
- Renamed the repository to `cookiecutter-pyproject`
- The new project now has its own documentation hosted on GitHub pages
- The documentation now includes more detailed information in favour of a shortened README.md
- Now uses `uv` as dependency manager
- Now uses justfile as taskrunner
- Now has extensive documentation on https://markusritschel.github.io/cookiecutter-pyproject/
- Uses Zensical for main documentation
