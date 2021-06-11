# {{cookiecutter.project_name}}

![main](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/main/badge.svg)
{% if cookiecutter.project_license != "No License" %}[![License {{ cookiecutter.project_license }}](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](./LICENSE){% endif %}


{{ cookiecutter.project_description}}


## Installation
Clone this repo via
```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```
Then, in the new directory (`cd {{ cookiecutter.project_slug }}/`) install the package via:
```
python setup.py install
```
or via
```
python setup.py develop
```
if you plan on making changes on the code.



## Project Structure

    ├── LICENSE            <- The license used for this project
    ├── Makefile           <- A self-documenting Makefile for standard CLI tasks
    ├── README.md          <- The top-level README of this project
    │
    ├── data               <- Contains all data used for the analyses in this project.
    │   │                     The sub-directories can be links to the actual location of your data.
    │   │                     However, they should never be under version control! (-> .gitignore)
    │   ├── interim        <- Intermediate data that have been transformed from the raw data
    │   ├── processed      <- The final, processed data used for the actual analyses
    │   └── raw            <- The original, immutable(!) data
    │
    ├── docs               <- Your documentation (default: Jupyter-Book; but feel free to use 
    │                         Sphinx or MkDocs or anything similar)
    │                         This should contain only documentation of the code and the assets.
    │                         A report of your actual project should be placed in `reports/book`.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     and a short `-` or `_` delimited description, e.g. `01-initial-analyses`
    │   ├── exploratory    <- Notebooks for exploratory tasks
    │   └── reports        <- Notebooks generating reports and figures
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated reports (e.g. HTML, PDF, LaTeX, etc.)
    │   ├── book           <- A Jupyter-Book describing your project
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── scripts            <- High-level scripts that use (low-level) source code from `src/`
    └── src                <- Source code (and only source code!) for use in this project
        ├── tests          <- Contains tests for the code in `src/`
        └── __init__.py    <- Makes src a Python module and provides some standard variables



## Testing
To test the code, run `make test` in the source directory.
This will execute both the unit tests and docstring examples (using pytest).

Run `make coverage` to generate a test coverage report and `make lint` to check code style consistency.


## Features
* [ ] TODO


## Maintainer
- [markusritschel](https://github.com/markusritschel)


## Contact & Issues
For any questions or issues, please contact me via {{ cookiecutter.email }} or open an [issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues).


---
&copy; {{ cookiecutter.full_name }} {% now 'local', '%Y' %}
