"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Set up new project from a cookiecutter template'])

