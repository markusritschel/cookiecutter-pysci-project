# Cookiecutter PySci-project Template
![build](https://github.com/markusritschel/cookiecutter-pysci-project/actions/workflows/main.yml/badge.svg)
[![License MIT](https://img.shields.io/github/license/markusritschel/cookiecutter-pysci-project)](./LICENSE)

> 👉 **DISCLAIMER:** If you're tired of setting up the same directory and file structure for your new scientific projects again and again, then this might be for you ;-)

This repository holds a "template" of a directory structure for small to medium-size scientific projects, making use of [CookieCutter](https://github.com/cookiecutter/cookiecutter), a templating engine for project structures.
Check out the links at the [bottom of the page](#sources-of-inspiration) to create your own CookieCutter or use this one to start your project.
Also, feel free to fork the repository and adjust it to your own needs.


***
## Table of contents <!-- omit in toc -->
- [Cookiecutter PySci-project Template](#cookiecutter-pysci-project-template)
  - [What is it good for? _or_ How this can boost your productivity](#what-is-it-good-for-or-how-this-can-boost-your-productivity)
  - [About this template](#about-this-template)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Setting up a new project](#setting-up-a-new-project)
    - [Using the Makefile](#using-the-makefile)
      - [Setting dependencies](#setting-dependencies)
    - [Snakemake](#snakemake)
    - [Write your documentation](#write-your-documentation)
      - [Using Sphinx](#using-sphinx)
        - [Best practise: Write documentation on a separate branch](#best-practise-write-documentation-on-a-separate-branch)
        - [Publish your documentation with Github pages 🚀](#publish-your-documentation-with-github-pages-)
      - [Using Jupyter-Book](#using-jupyter-book)
      - [Using both a (Jupyter book) report alongside your code documentation as Github page](#using-both-a-jupyter-book-report-alongside-your-code-documentation-as-github-page)
    - [Some tips and thoughts regarding the code layout](#some-tips-and-thoughts-regarding-the-code-layout)
  - [Project Structure](#project-structure)
  - [Dummy files](#dummy-files)
  - [Sources of inspiration](#sources-of-inspiration)
  - [Contributing](#contributing)

***

## What is it good for? _or_ How this can boost your productivity
[CookieCutter](https://cookiecutter.readthedocs.io/) is a templating engine for creating directory structures including pre-defined files based on a question catalogue that is being asked during the setup.<br>
By running `cookiecutter` with this repository, a new directory will be created with a pre-defined structure and some basic files, making you all ready for starting a new scientific python project without having to manually create the same files & structure over and over again.
This includes
- code that is importable from every place in your environment
- automatically resolved paths to the project's root and the directories for data, plots, logs, etc.
- `make` commands to run automated unit tests, create documentation of your code, etc.
- creating a nice HTML representation of your Jupyter notebooks and of your doc strings
- and so on... 🚀

> **Note**: 
> CookieCutter seems to be on hiutus at the moment, meaning that the maintainers are not working on it anymore. While it should still work, you can also switch to the fork [CookieNinja](https://github.com/cookieninja-generator/cookieninja), which works with cookiecutters (project templates) the same way as the original CookieCutter does. 

## About this template
There exist tons of different CookieCutter templates for all different kinds of projects.
However, according to my experience, many of them are very complex in their structure and therefore often a bit overkill, especially for new-comers or projects of a rather modest size.
<br>
This template provides a boilerplate for small to medium-size (scientific) data projects, e.g. a thesis, a group project, or similar.
For an overview of the directory & file structure have a look at the [section further below](#project-structure).
The redundant parts (mainly for demonstration purposes) are only few and are listed in the section after the one describing the project structure.

> 👉 Once set up, a Git repository is automatically initialized. 
If you want to connect it with a remote repository on GitHub (or any other hosted git service) you need to [add the respective remote repository to your local repository](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories).

## Requirements
You need to have python installed as well as the python package `cookiecutter`.
You can do this either via pip or conda.
```bash
$ pip install -U cookiecutter cruft
$ conda install -c conda-forge cookiecutter cruft
```
As mentioned above, instead of `cookiecutter` you can also use `cookieninja`.
Besides that, there is no need to clone or download anything from this repository. Just follow the next step :-)

> 👉 **Important hint**: I recommend you to install [Mamba](https://mamba.readthedocs.io/) as a package manager. It is build on `conda` but has a much greater performance.


## Usage
If you plan to use git as a version control system, ensure that you have installed it on your machine and that you have specified the Git configuration settings:
```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
### Setting up a new project
Then, after having `cookiecutter` installed, create a new project from this template by executing one of the following commands:
```bash
$ cookiecutter gh:markusritschel/cookiecutter-pysci-project
$ cookiecutter https://github.com/markusritschel/cookiecutter-pysci-project.git
$ cookiecutter git+https://github.com/markusritschel/cookiecutter-pysci-project
$ cookiecutter git+ssh://git@github.com/markusritschel/cookiecutter-pysci-project.git
```
The script will ask you some questions based on the entries in the `cookiecutter.json` and will then create a new project based on this template with the information that you just provided by answering the questions.
Finalize the step by changing to the new directory.

> 👉 For the following steps, there are also Make commands available that ease the work for you.

Then, for development, I **strongly** recommend you create a dedicated virtual environment. 
Using conda, you can simply execute `conda create -n <your-environment-name>` or create an environment based on the environment.yml file by executing `conda create -f environment.yml`. 
The latter would create a virtual conda environment with the same name as your project directory. 
You can override the default name of the environment with the option `-n <your-custom-name>`.
This should also install all the required packages that you need to make your new project work, including generating the documentation.

You finalize the set up by activating the environment via `conda activate <your-environment-name>`.

> 👉 You can use the pre-defined commands `make setup-conda-env` and `make src-available` instead of performing the above steps manually.
> See also the README.md of your new project.

For further information you may wanna have a look at the README.md file in the root directory of your new project.
This will give you more information about setting up the project, making your code installable, etc.
You may also want to check out the Makefile commands (simply type `make` to get an overview of the available commands).

### Using the Makefile
The Makefile in the project directory provides some default routines like cleanup, testing, installing requirements etc.
<br>
Even though for many people using `make` seems to be a bit old-fashioned, I would recommend you have a look at Make's great capability of dealing with dependencies.
This is in particular useful if, for example, the first step in your data-processing pipeline takes a long time to process your raw data and generate the interim product.
<br>
I usually structure my data-processing workflow such that I can run a single process via command line (for example `python scripts/process-raw-data.py -o ./output_dir`). 
(The python packages `click`, `fire` and `docopt` provide neat functionalities to convert your scripts into interactive command-line interfaces.)
These commands I can set as targets in the Makefile, for example:
```make
## Process raw data and write the newly generated data into ./data/interim/
process_raw_data:
    python scripts/process-raw-data.py
```
I can now simply run `make process_raw_data` in the project's root directory.

#### Setting dependencies
Let's assume that the previous step (processing the raw data) generates new data inside `./data/interim/`. If I now have a second processing step that depends on the data generated by the previous step, I can set these data as dependencies for the new rule:
```make
## Process interim data
process_interim_data: $(wildcard data/interim/**/*)
    python scripts/process-interim-data.py
```
This way, the last step is only executed if the data it depends on have changed since the last time of execution.

For further information, have a look at Make's documentation: https://www.gnu.org/software/make/manual/html_node/Rules.html


### Snakemake
Additionally to `make` or as an alternative, [Snakemake](https://snakemake.readthedocs.io) provides even more extended functionalities. 
The syntax used in Snakemake is pure python, making it very convenient to work with and providing all the functionality of Python in your Snakemake workflow.
In Snakemake you define dependencies not as an "artificial" target but you indicate the target file you want to create, and Snakemake takes care of producing the required dependencies.
Another strength of Snakemake is that it is easily scalable.
Porting your Snakemake workflow from your local machine to a High Performance Computing system is as straightforward as adding a few extra parameters to the executed command.
This way, Snakemake automatically generates bash scripts and submits them as jobs on the HPC, automatically distributing the tasks of the workflow.  <!-- todo -->

### Write your documentation 
In my opinion it is helpful to differentiate between two kinds of documentation: 
1. The first kind should only **document your code** (similar to what you would expect when opening the online documentation of a python package or similar) and should be considered as best practice to be shipped with your code.
2. The second is optional but, in my opinion, possibly very helpful for others (and also for yourself) to understand **what is going on in your project**, present your results etc..
<!-- todo: Verweis auf die "BES: Guides to Better Science" Serie -->

For the first, I would recommend you to use [Sphinx](https://www.sphinx-doc.org/), which is particularly suited for documenting python code and already set up as default doc engine in this project template. It's _autodoc_ extension can also parse the doc strings of your code and process them to nice HTML output. For more details, see the [section below](#using-sphinx).

For the second purpose you can, in principle, use whichever tool you like the most (Sphinx, MkDocs, Jekyll, etc.). I personally like [Jupyter Book](https://jupyterbook.org/) very much as it is feature-rich and you can use a bunch of languages: Jupyter Markdown, MyST Markdown for more publishing features, reStructuredText, even your Jupyter Notebooks, or any Jupytext format.

#### Using Sphinx
In short: describe as much of your code as possible in the doc-strings of your functions, classes and modules.
Sphinx can then parse these doc-strings and format them nicely in your documentation output. 
To compile an HTML report of your Sphinx documentation locally, enter the `docsrc` directory and execute `make html` (type `make` for more formats).
Alternatively you can run `make docs` from the root of your project.
**Hint:** If you use Github for your project, I have integrated a workflow for automatic deployment. The only thing, you need to prepare is, go into your repository's settings (on Github), go to _Pages_ and then select "Deploy from a branch" for _Source_ and under _Branch_ select "gh-pages" and "root". Save your changes. Now, whenever you push something to the main branch, your documentation in `docsrc` will be automatically compiled and deployed. The result will be available on https://<your-github-username>.github.io/<your-project-name>
For a detailed description of how to use Sphinx and how to write your documentation check out their [website](https://www.sphinx-doc.org/).

##### <u>Best practise:</u> Write documentation on a separate branch
I would suggest that you create a separate `docs` branch for writing your documentation in order to keep them separated from your code progress.
To write on your documentation, you would then always switch to the `docs` branch. 
Remember to always merge your current main branch to ensure Sphinx can parse the most up-to-date version!

##### Publish your documentation with [Github pages](https://pages.github.com/) 🚀
Github allows you to host static websites on their platform.
In this project template, I have integrated a workflow for automatic deployment. 
The only thing you need to prepare is, go into your repository's settings (on Github), go to _Pages_ and then select "Deploy from a branch" for _Source_ and under _Branch_ select "gh-pages" and "root". Save your changes. \
Now, whenever you push something to the main branch, your documentation in `docsrc` will be automatically compiled and deployed. The result will be available on `https://<your-github-username>.github.io/<your-project-name>`. Magic… 🪄😉 

> **Note**\
> Keep in mind that the deployment may take a while. You can check the status of the workflow by clicking on "Action" in the menu bar of your repository.

#### Using Jupyter-Book
To compile your jupyter book, simply execute `jb build reports/book` or `make book` from the root of your project.
Alternatively to your source code documentation, you can also place the content of your compiled jupyter book to `docs/` to publish it via Github pages.

#### Using both a (Jupyter book) report alongside your code documentation as Github page
_Github pages_ allows only one website per repository. Usually that can be accessed via the domain https://your-github-usernam.github.io/your-project.
To use both your project html report (Jupyter book) _and_ your technical code documentation, you can merge the two compiled html outputs.
For example, to have your project report as the main site on your repository's domain, put the content of your compiled jupyter book (found in `reports/book/_build/html`) in `./docs` (inside the repository's root) and put the Sphinx-compiled code documentation (found in `docsrc/_build/html`) into a subfolder of `.docs/` (e.g. `./docs/code-documentation`). 
Then, your project report will be found on the repository's github page (https://your-github-usernam.github.io/your-project) and your code documentation on https://your-github-usernam.github.io/your-project/code-documentation, respectively.
You could then link your code documentation on your jupyter-book page or make the link somewhere else available.


> 📔 **Side note**<br>
> _Jupyter Book_ can also be a nice way to share your collection of Jupyter notebooks online.
There are plugins that allow people to comment on the rendered HTML representation of your notebooks.


### Some tips and thoughts regarding the code layout
All scripts and Jupyter notebooks that deal with either processing of the data or the creation of any kind of reports (plots, documents, etc) should reside in the `scripts/` and `notebooks/` directory, respectively.<br>
Code under `src/` is _exclusively_ source code (i.e. low-level code) and is not directly run.<br>
Name scripts and the notebooks in a way that indicates their order of execution (examples can be found in the respective directories).
It is also recommended to have _one_ script for each task, i.e. the creation of _one_ figure or _one_ table.

> ⚠️ **A note on version controlling Jupyter notebooks**<br>
It is very ugly to keep Jupyter notebooks under version control as they are in principle a very large JSON file, containing lots of metadata, output of your cells etc. This circumstance makes it also quite hard to collaborate on them. However, a while ago I stumbled upon _[Jupytext](https://jupytext.readthedocs.io/)_ which syncs your jupyter notebooks with another file for which you can choose a variety of formats (e.g. Markdown, R Markdown, normal python, etc.). These "paired" files can either resider alongside your jupyter notebooks or in a separate directory.
_Jupytext_ can either be used from the command line (`jupytext --sync notebooks/*ipynb`) or as a jupyter plugin. 
For more information, have a look on their [documentation site](https://jupytext.readthedocs.io/).

## Project Structure

    ├── assets             <- A place for assets like shapefiles or config files
    │
    ├── data               <- Contains all data used for the analyses in this project.
    │   │                     The sub-directories can be links to the actual location of your data.
    │   │                     However, they should never be under version control! (-> .gitignore)
    │   ├── interim        <- Intermediate data that have been transformed from the raw data
    │   ├── processed      <- The final, processed data used for the actual analyses
    │   └── raw            <- The original, immutable(!) data
    │
    ├── docsrc             <- The technical documentation (default engine: Sphinx; but feel free to 
    │                         use MkDocs, Jupyter-Book or anything similar).
    │                         This should contain only documentation of the code and the assets.
    │                         A report of the actual project should be placed in `reports/book`.
    │
    ├── logs               <- Storage location for the log files being generated by scripts
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     and a short `-` or `_` delimited description, e.g. `01-initial-analyses`
    │   ├── _paired        <- Optional location for your paired jupyter notebook files
    │   ├── exploratory    <- Notebooks for exploratory tasks
    │   └── reports        <- Notebooks generating reports and figures
    │
    ├── references         <- Data descriptions, manuals, and all other explanatory materials
    │
    ├── reports            <- Generated reports (e.g. HTML, PDF, LaTeX, etc.)
    │   ├── book           <- A Jupyter-Book describing the project
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── scripts            <- High-level scripts that use (low-level) source code from `src/`
    ├── src                <- Source code (and only source code!) for use in this project
    │   ├── tests          <- Contains tests for the code in `src/`
    │   └── __init__.py    <- Makes src a Python module and provides some standard variables
    │
    ├── .env               <- In this file, specify all your custom environment variables
    │                         Keep this out of version control! (i.e. have it in your .gitignore)
    ├── .gitignore         <- Here, list all the files, folders (patterns allowed) that you want to
    │                         keep out of git version control.    
    ├── CHANGELOG.md       <- All major changes should go in there
    ├── jupytext.toml      <- Configuration file for jupytext
    ├── LICENSE            <- The license used for this project
    ├── Makefile           <- A self-documenting Makefile for standard CLI tasks
    ├── README.md          <- The top-level README of this project
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── setup.py           <- Setup python file to install your source code in your (virtual) python 
                              environment


## Dummy files
The following files are for demonstration purposes only and, if not needed, can be deleted safely:

    ├── notebooks/01-minimal-example.ipynb
    ├── docsrc/*
    ├── reports/book/*
    ├── scripts/01-test.py
    └── src
        ├── tests/*
        └── submodule.py


## Sources of inspiration
Some great sources of inspiration and orientation when I created this template:
- A great article on how to structure your scientific data projects: https://drivendata.github.io/cookiecutter-data-science
- https://github.com/drivendata/cookiecutter-data-science
- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://github.com/hackalog/easydata
- https://github.com/aubricus/cookiecutter-python-package
- https://github.com/cookieninja-generator/cookieninja


## Contributing
Issues & pull-requests accepted.


---
&copy; [Markus Ritschel](https://github.com/markusritschel), 2023
