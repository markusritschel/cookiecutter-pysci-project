"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Set up new project from cookiecutter template https://github.com/markusritschel/cookiecutter-pysci-project'])
print("If you want to add a remote repository, run `git remote add origin https://github.com/"
      "{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}` (maybe modify the address)")
