# Cookiecutter PySci-project Template
[![License MIT](https://img.shields.io/github/license/markusritschel/cookiecutter-pysci-project)](./LICENSE)

_Just another [CookieCutter](https://github.com/cookiecutter/cookiecutter) Template for Scientific Python Projects._

CookieCutter is a templating engine for creating directory structures including pre-defined files based on a question catalogue that are being asked during the setup.<br>
By running `cookiecutter` with this repository, a new directory will be created with a pre-defined file structure and some basic files, making you all ready for starting a new scientific python project.<br>

## Requirements
You need to have python installed as well as the python package `cookiecutter`.
You can do this either via pip or conda.
```bash
$ pip install -U cookiecutter
$ conda install -c conda-forge cookiecutter
```
Besides that, there is no need to clone or download anything from this repository. Just follow the next step :-)

## Usage
After having cookiecutter installed, create a new project from this template by executing one of the following commands:
```bash
$ cookiecutter gh:markusritschel/cookiecutter-pysci-project
$ cookiecutter https://github.com/markusritschel/cookiecutter-pysci-project.git
$ cookiecutter git+https://github.com/markusritschel/cookiecutter-pysci-project
$ cookiecutter git+ssh://git@github.com/markusritschel/cookiecutter-pysci-project.git
```
The script will ask you some questions based on the entries in the `cookiecutter.json` and will then create a new project based on this template with the information you have just given by answering the questions.

## Maintainer
- [markusritschel](https://github.com/markusritschel)

## Contributing
Issues & pull-requests accepted.


---
&copy; Markus Ritschel 2021
