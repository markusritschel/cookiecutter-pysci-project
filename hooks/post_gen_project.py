"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import os
import shutil
import subprocess

if not {{ cookiecutter.is_research_project }}:
    REMOVE_PATHS = [
        "data/",
        "logs/",
        "notebooks/",
        "references/",
        "reports/",
        "scripts/",
    ]
    for path in REMOVE_PATHS:
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)


print("Initialize Git repository and make a first commit")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Set up new project from cookiecutter template https://github.com/markusritschel/cookiecutter-pysci-project'])

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

print(GREEN)
print("="*100)
print("")

print(f"  ✅ The project is all set now.")
print(f"     Please navigate now to the new directory {os.getcwd()}/. ")

print(f"  👉 If you want to add a remote git repository, run \n" + 
      f"       {BLUE}git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }} \n" + GREEN +
      f"     from the new directory.")

print("  👉 It is furthermore recommended to work in a virtual environment (hint: run `make` to get help).")
print("  ℹ️ For further information on how to use the project, please check the README.md file.")
      
print("")
print("="*100)
print(RESET)
