"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import subprocess

print("Initialize Git repository and make a first commit")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Set up new project from cookiecutter template https://github.com/markusritschel/cookiecutter-pysci-project'])
print("If you want to add a remote repository, run `git remote add origin https://github.com/"
      "{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}` (maybe modify the address)")

print("The project is all set. It is recommended to create a conda environment. You can do this "
      "either manually or by running the respective command from the Makefile (hint: run `make` to get help).")
      