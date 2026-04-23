"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import os
import shutil
import subprocess


# /// 1. Remove redundant paths ///

def remove_recursively(paths):
    for path in paths:
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)

sphinx_files = [
    'docs/conf.py',
    'docs/_config/',
    'docs/changelog.md',
    
]
zensical_files = [
    'zensical.toml'
]
myst_files = [
    'docs/myst.yml'
]
research_project_files = [
    'data/',
    'notebooks/',
    'references/',
    'reports/',
    'scripts/'
]

if not {{ cookiecutter.is_research_project }}:
    remove_recursively(research_project_files)

if "{{ cookiecutter.docs_engine|lower }}" == "sphinx":
    remove_recursively(zensical_files)
    remove_recursively(myst_files)
elif "{{ cookiecutter.docs_engine|lower }}" == "zensical":
    remove_recursively(sphinx_files)
    remove_recursively(myst_files)

elif "{{ cookiecutter.docs_engine|lower }}" == "myst":
    remove_recursively(sphinx_files)
    remove_recursively(zensical_files)


# /// 2. Initialize Git repository ///

if not os.path.exists(".git"):
    print("Initialize Git repository and make a first commit")
    subprocess.run(["git", "init"], check=True)
    subprocess.run(['git', 'branch', '-m', 'main'], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Set up new project from cookiecutter template https://github.com/markusritschel/cookiecutter-pyproject"], check=True)


# /// 3. Print message ///

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

DEFAULT = GREEN
CODE = BLUE

msg = f"""
    🎉 Project setup complete! How to get started:
    ----------------------------------------------

    1. Change directory into your project (if you aren't already):
        {CODE}cd {os.getcwd()}/ {DEFAULT}

    2. Activate your virtual environment (see the README.md for more details):
        On Linux/macOS: {CODE}source .venv/bin/activate {DEFAULT}
        On Windows:    {CODE}.\.venv\Scripts\\activate {DEFAULT}

    3. Add a remote git repository (optional): {CODE}
        {CODE}git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }} {DEFAULT}

    4. To add packages, use:
        {CODE}uv add <package_name> {DEFAULT}

    5. To run scripts, use:
        {CODE}uv run python <script.py> {DEFAULT}

    6. To build documentation:
        {CODE}just docs {DEFAULT}


    Happy coding! 🚀
"""

print(GREEN)
print("="*100)
print(msg)
print("")
print("="*100)
print(RESET)

