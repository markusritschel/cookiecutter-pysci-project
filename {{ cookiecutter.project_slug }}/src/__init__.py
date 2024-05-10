# !/usr/bin/env python3
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.project_author }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
import sys
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from .core.utils import setup_logger

__version__ = '{{ cookiecutter.project_version }}'

# Make some of the basic directories globally available in your environment
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'
LOG_DIR  = BASE_DIR / 'logs'
PLOT_DIR = BASE_DIR / 'reports/figures'
jupyter_startup_script = BASE_DIR / 'notebooks/jupyter_startup.ipy'

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)

sys.path.append(str(BASE_DIR/"scripts"))



welcome = """
████████╗██╗████████╗██╗     ███████╗
╚══██╔══╝██║╚══██╔══╝██║     ██╔════╝
   ██║   ██║   ██║   ██║     █████╗  
   ██║   ██║   ██║   ██║     ██╔══╝  
   ██║   ██║   ██║   ███████╗███████╗
   ╚═╝   ╚═╝   ╚═╝   ╚══════╝╚══════╝
          Some subtitle ☃
"""
# https://patorjk.com/software/taag/ with "ANSI Shadow" font

# print(pyfiglet.figlet_format("My title", font="slant") + "\n Some subtitle")


if __name__ == '__main__':
    print(welcome)
