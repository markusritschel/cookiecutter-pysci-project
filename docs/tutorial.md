---
icon: material/school
---

# Tutorial

??? note "Requirements"
    - [uv](https://docs.astral.sh/uv/)
    - [git](https://git-scm.com/) with initial configuration. Run
      ```text
      $ git config --global user.name "John Doe"
      $ git config --global user.email johndoe@example.com
      ```
      with your name and e-mail.
    - [just](https://just.systems/) (optional but recommended)
    - [GitHub](https://github.com/) account (optional)


## Create a new project using the template
Make sure to have `uv` installed, and then run the following command to create a new project from this template:
```bash
uvx --with jinja2-time copier copy --trust gh:markusritschel/cookiecutter-pyproject my-project
```
This generates the project in a new `my-project/` directory — replace `my-project` with the directory name you want.

!!! warning "`--trust` is required"
    The template uses the `jinja2-time` Jinja extension (for the copyright year in `LICENSE` and
    `CITATION.cff`) and runs a post-generation task (`git init` + first commit, `uv sync --dev`,
    pre-commit installation). copier treats both as unsafe and aborts with
    `Template uses potentially unsafe features: jinja_extensions, tasks` unless you pass `--trust`.
    Nothing is generated in that case.

<!-- Alternative URIs:
copier copy --trust https://github.com/markusritschel/cookiecutter-pyproject.git my-project
copier copy --trust git+ssh://git@github.com/markusritschel/cookiecutter-pyproject.git my-project
-->

copier then asks you a series of questions to customize your project (see [Prompts](prompts.md) for what each one means).
Free-text questions show their default in parentheses — press <kbd>Enter</kbd> to accept it or type your own value.
Choice questions (CLI library, license, docs engine) are selected with the arrow keys.
A typical run looks like this:

```
🎤 Your full name
   Your Name
🎤 Your email address
   your@e.mail
🎤 Your GitHub username
   your-github-username
🎤 The human-readable name of your project (spaces allowed)
   My Cool Package
🎤 The directory and repository name (derived from the project name)
   my-cool-package
🎤 The importable Python package name (derived from the project slug)
   my_cool_package
🎤 Is this a research project? (adds data/, notebooks/, references/, reports/, scripts/) (Y/n)
   Yes
🎤 A short description of your project
   A boilerplate for scientific projects using Python
🎤 The initial version of your project
   0.1.0
🎤 Which command-line interface library would you like to use?
   No command-line interface
🎤 Choose a license for your project
   MIT license
🎤 Which documentation engine would you like to use?
   Sphinx
```

The values shown are the defaults. For the two choice questions with real alternatives, pick
deliberately: `command_line_interface` decides whether a `cli.py` and a `[project.scripts]` entry
point are generated (Typer, Click or Docopt), and `docs_engine` selects between Sphinx, Zensical and
MyST — which determines the contents of `docs/`, the `docs` dependency group and the build commands
behind `just docs`. See [Prompts](prompts.md) for the full reference.

If everything goes well, you should see a message like this at the end of the setup process:

```toml
🎉 Project setup complete! How to get started:
----------------------------------------------

1. Change directory into your project (if you aren't already):
     cd my-project/ 

2. Activate your virtual environment (see the README.md for more details):
     On Linux/macOS: source .venv/bin/activate 
     On Windows:    .\.venv\Scripts\activate 

3. Add a remote git repository (optional):  # (1)!
     git remote add origin https://github.com/<your-github-username>/<package-slug> 

4. To add packages, use:
     uv add <package_name> 

5. To run scripts, use:
     uv run python <script.py> 

6. To build documentation:
     just docs

Happy coding! 🚀

```

1. Visit the official [github documentation](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories) for more details

The template will already have a git repository initialized in your new project directory.
You can now add a remote repository and push your new project to GitHub.
