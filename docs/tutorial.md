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
uvx cookiecutter gh:markusritschel/cookiecutter-pyproject
```
<!-- Alternative URIs:
cookiecutter gh:markusritschel/cookiecutter-pyproject
cookiecutter https://github.com/markusritschel/cookiecutter-pyproject.git
cookiecutter git+https://github.com/markusritschel/cookiecutter-pyproject
cookiecutter git+ssh://git@github.com/markusritschel/cookiecutter-pyproject.git
-->

Fill in the prompts to customize your project. For example:

```
  [1/12] project_author (Markus Ritschel): Your name
  [2/12] email (git@markusritschel.de): your@e.mail
  [3/12] github_username (markusritschel): your-github-username
  [4/12] project_name (Python Boilerplate): My Cool Package
  [5/12] project_slug (python-boilerplate): my-cool-package
  [6/12] package_name (python_boilerplate): my_cool_package
  [7/12] is_research_project [y/n] (y): 
  [8/12] project_description (A boilerplate for scientific projects using Python): 
  [9/12] project_version (0.1.0): 
  [10/12] Select command_line_interface
    1 - Click
    2 - Docopt
    3 - No command-line interface
    Choose from [1/2/3] (1): 
  [11/12] Select project_license
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from [1/2/3/4/5/6] (1): 
  [12/12] Select docs_engine
    1 - Sphinx
    2 - Zensical
    3 - MyST
    Choose from [1/2/3] (1):
```

If everything goes well, you should see a message like this at the end of the setup process:

```toml
🎉 Project setup complete! How to get started:
----------------------------------------------

1. Change directory into your project (if you aren't already):
     cd /tmp/<package-slug>/ 

2. Activate your virtual environment (see the README.md for more details):
     On Linux/macOS: source .venv/bin/activate 
     On Windows:    .\.venv\Scriptsctivate 

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
