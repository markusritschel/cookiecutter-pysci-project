"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import subprocess
import os
from colorama import Fore, Back, Style

print("Initialize Git repository and make a first commit")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Set up new project from cookiecutter template https://github.com/markusritschel/cookiecutter-pysci-project'])

print(Fore.GREEN)
print("="*100)
print("")

print(f"  ✅ The project is all set now. Please navigate now to the new directory {os.getcwd()}/. ")

print("  👉 If you want to add a remote git repository, run \n" + Fore.BLUE +
      "       git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }} \n" + Fore.GREEN +
      "     from the new directory.")

print("  👉 It is furthermore recommended to create a conda environment (hint: run `make` to get help).")
      
print("")
print("="*100)
