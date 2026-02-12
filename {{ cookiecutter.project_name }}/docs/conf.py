project = "{{ cookiecutter.project_name }}"
author = "{{ cookiecutter.project_author }}"
copyright = "{% now 'utc', '%Y' %}"
title = "{{ cookiecutter.project_name }} Documentation 2"
html_title = "Sidebar title"
html_logo = "_static/python-logo.svg"


html_theme = "{{ cookiecutter.sphinx_theme }}"   # furo, sphinx_rtd_theme, pydata_sphinx_theme, sphinx_book_theme, sphinx_immaterial
master_doc = 'index'
html_static_path = ["_static"]
templates_path = ['_templates']
exclude_patterns = ['_build', '_autoapi']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# https://pygments.org/styles/
pygments_style = 'default'
pygments_dark_style = 'zenburn'

# Default extensions
extensions = [
    'nbsphinx',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinxcontrib.mermaid',
    # 'sphinx_jupyterbook_latex',
    # 'sphinx.ext.autodoc.typehints',
    # 'sphinx.ext.linkcode',
    # 'sphinx.ext.todo',
    # 'sphinx_issues',
]


html_theme_options = {
    # see the respective theme configuration files in _config/themes/ for more options
}

nb_custom_formats = {
    '.md': [
        'jupytext.reads',
        'fmt: myst',
    ],
}
 

from pathlib import Path
import sys
import importlib


sys.path.append(str(Path(__file__).parent))

try:
    module = importlib.import_module("_config.themes."+html_theme)
    # html_theme_options = getattr(module, "html_theme_options", {})
    # html_theme_options.update(_html_theme_options)
    # html_css_files = getattr(module, "html_css_files", {})
    # extensions += getattr(module, "extensions", [])

    if hasattr(module, "extensions"):
        extensions += getattr(module, "extensions", [])
        delattr(module, "extensions")  # Remove the extensions variable to avoid conflicts

    # Extract only non-function variables
    module_vars = {k: v for k, v in vars(module).items() 
                   if not k.startswith('_')}
    globals().update(module_vars)
    
except ModuleNotFoundError:
    print(f"Warning: No specific configuration found for theme '{html_theme}'.")

# Configurations to include from _config/
_configs = [
    # 'autodoc2',   # !! Don't include autodoc2 and autoapi at the same time, as they conflict with each other. 
    'autoapi',
    'bibtex',
    'images',
    'intersphinx',
    'myst',
    'napoleon',
    'typehints',
]
for config in _configs:
    module = importlib.import_module("_config."+config)
    if hasattr(module, "extensions"):
        extensions += getattr(module, "extensions", [])
        delattr(module, "extensions")  # Remove the extensions variable to avoid conflicts

    # Extract only non-function variables
    module_vars = {k: v for k, v in vars(module).items() 
                   if not k.startswith('_')}
    globals().update(module_vars)
    