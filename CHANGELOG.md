# Change Log

## Unreleased

- Migrated the template engine from cookiecutter (+ cruft for updates) to [copier](https://copier.readthedocs.io)
- Project generation now uses `uvx --with jinja2-time copier copy gh:markusritschel/cookiecutter-pyproject my-project`
- Template updates now use `copier update` (replacing `cruft update`), tracked via the generated `.copier-answers.yml`
- Removed `cookiecutter.json` and the `hooks/` directory; prompts, conditional generation, and post-generation setup are now defined in `copier.yml`
- Replaced the inline POSIX-shell post-generation `_tasks` (git init/commit, `uv sync --dev`, pre-commit install) with a standalone `tasks/post_gen.py`, so project generation also works on native Windows without WSL/git-bash; the simpler inline-shell approach was considered but rejected for not being cross-platform
- Updated all user-facing documentation (README, docs site) to the copier workflow
- Fixed the `package_name` validator in `copier.yml`: it used a regex (`^[_a-zA-Z][_a-zA-Z0-9]+$`) that required at least two characters and only allowed ASCII, so it rejected valid single-character (e.g. `x`) and non-ASCII (PEP 3131) package names. Replaced it with `package_name.isidentifier()`, which matches Python's own identifier grammar exactly. Rejected patching the regex in place (e.g. `[_a-zA-Z0-9]*`) since it would still be ASCII-only and require hand-updating for any future identifier edge case.
- Added `LICENSE` and `CITATION.cff` to `copier.yml`'s `_skip_if_exists` so their `{% now %}`-stamped copyright year / release date aren't silently rewritten on `copier update`

## 1.0.0

- Merged two repositories ([cookiecutter-pypackage](https://github.com/markusritschel/cookiecutter-pypackage) & [cookiecutter-pysci-project](https://github.com/markusritschel/cookiecutter-pysci-project))
- Renamed the repository to `cookiecutter-pyproject`
- The new project now has its own documentation hosted on GitHub pages
- The documentation now includes more detailed information in favour of a shortened README.md
- Now uses `uv` as dependency manager
- Now uses justfile as taskrunner
- Now has extensive documentation on https://markusritschel.github.io/cookiecutter-pyproject/
- Uses Zensical for main documentation
