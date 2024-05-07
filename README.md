# Cookiecutter Py(thon)Sci(ence)-Project Template <!-- omit in toc -->

![build](https://github.com/markusritschel/cookiecutter-pysci-project/actions/workflows/main.yml/badge.svg)
[![License MIT](https://img.shields.io/github/license/markusritschel/cookiecutter-pysci-project)](./LICENSE)

> 👉 If you're tired of setting up the same directory and file structure for your new scientific projects again and again, then this might be for you ;-)

This repository provides a "template" of a directory structure for small to medium-sized scientific projects, making use of [CookieCutter](https://github.com/cookiecutter/cookiecutter), a templating engine for project structures.
Check out the links at the [bottom of the page](#sources-of-inspiration) to create your own CookieCutter or use this one to start your project.
Also, feel free to fork the repository and adjust it to your own needs.

***

## <u>Table of contents</u> <!-- omit in toc -->

- [What is it good for? _or_ How this can boost your productivity](#what-is-it-good-for-or-how-this-can-boost-your-productivity)
- [About this template](#about-this-template)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Preparations](#preparations)
  - [Setting up a new project](#setting-up-a-new-project)
    - [Creating the project structure](#creating-the-project-structure)
    - [Creating the code environment](#creating-the-code-environment)
  - [Make \& Snakemake](#make--snakemake)
    - [Using the Makefile](#using-the-makefile)
    - [Setting dependencies](#setting-dependencies)
    - [Snakemake](#snakemake)
  - [Document your project](#document-your-project)
    - [What tool should I use?](#what-tool-should-i-use)
      - [For technical documentation](#for-technical-documentation)
      - [For scientific publications](#for-scientific-publications)
    - [Publish your documentation with Github pages](#publish-your-documentation-with-github-pages)
  - [Some tips and thoughts regarding the code layout](#some-tips-and-thoughts-regarding-the-code-layout)
    - [High-level \& low-level Code](#high-level--low-level-code)
- [Project Structure](#project-structure)
- [Dummy files](#dummy-files)
- [Sources of inspiration](#sources-of-inspiration)
- [Contributing](#contributing)

***

## What is it good for? _or_ How this can boost your productivity

[CookieCutter](https://cookiecutter.readthedocs.io/) is a templating engine for creating directory structures including pre-defined files based on a set of questions asked during the setup.<br>
By running `cookiecutter` with this repository, a new directory will be created with a pre-defined structure and some default files, making you all set to start a new scientific Python project without having to manually create the same files & structure over and over again.
This includes

- code that is importable from every place in your environment
- automatically resolved paths to the project's root and the directories for data, plots, logs, etc.
- `make` commands to run automated unit tests, create documentation of your code, etc.
- creating a nice HTML representation of your Jupyter notebooks and of your doc strings
- and so on... 🚀

It is indeed so easy:<br>
![cookiecutter](assets/cookiecutter.gif)

## About this template

This template provides a boilerplate for small to medium-size (scientific) data projects, e.g. a thesis, a group project, or similar.
For an overview of the directory & file structure have a look at the [section further below](#project-structure).
The redundant parts (mainly for demonstration purposes) are [only few](#dummy-files) and and can be safely removed.

> [!NOTE]
> Once set up, a Git repository is automatically initialized.
If you want to connect it with a remote repository on GitHub (or any other hosted git service) you need to [add the respective remote repository to your local repository](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories).

## Requirements

You need to have Python installed as well as the Python package `cookiecutter`.
You can do this either via pip or conda:

```bash
$ pip install -U cookiecutter cruft
$ conda install -c conda-forge cookiecutter cruft
```

`cruft` is optional. It is a tool that helps you to update your project template to the latest version. More details can be found on https://cruft.github.io/cruft/.

Besides that, there is no need to clone or download anything from this repository. Just follow the next step :-)

> [!TIP]
> I recommend you to install [Mamba](https://mamba.readthedocs.io/) as a package manager. It is built on `conda` but has a much greater performance.

## Usage

### Preparations

If you plan to use Git as a version control system, ensure that you have it installed on your machine and that you specified the global Git configuration settings (this needs to be done only once):

```bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

### Setting up a new project

#### Creating the project structure

After having `cookiecutter` installed, create a new project from this template by executing one of the following commands:

```bash
$ cookiecutter https://github.com/markusritschel/cookiecutter-pysci-project.git
$ cookiecutter gh:markusritschel/cookiecutter-pysci-project
$ cookiecutter git+https://github.com/markusritschel/cookiecutter-pysci-project
$ cookiecutter git+ssh://git@github.com/markusritschel/cookiecutter-pysci-project.git
```

Follow the instructions.
You will be asked some questions based on the entries in the `cookiecutter.json`.

Once, done, you have a fresh directory structure, modified with the information you just provided to CookieCutter.

#### Creating the code environment

You should now create a new/dedicated virtual environment either with `conda` (for better performance use `mamba`) or `pipenv` or something similar.
For a `conda` environment, you can simply execute

```bash
make conda-env
```

This should create a conda environment named after your project.
Alternatively, create your environment manually.

Now install the required packages via

```bash
make install-requirements
```

Finally, to make the source code in `src` available for import, execute

```bash
make src-available
```

💪 You are now all set to start with your new project 🚀.

> [!TIP]
> For further information, see also the README of your new project.
> You may also want to check out the Makefile commands (simply type `make` to get an overview of the available commands).

### Make & Snakemake

#### Using the Makefile

The Makefile in the project directory provides some default routines like cleanup, testing, installing requirements, etc.
<br>
Even though for many people using `make` may seem a bit old-fashioned, I would recommend you have a look at Make's great capability of dealing with dependencies.
This is particularly useful if, for example, the first step in your data-processing pipeline takes a long time to process your raw data and generate the interim product.
<br>
I usually structure my data-processing workflow such that I can run a single process via the command line (for example `python scripts/process-raw-data.py -o ./output_dir`). 
(The Python packages [click](https://click.palletsprojects.com/), [fire](https://google.github.io/python-fire/), and [docopt](http://docopt.org/) provide neat functionalities to convert your scripts into interactive command-line interfaces.)
These commands I can then set as targets in the Makefile, for example:

```make
## Process raw data and write the newly generated data into ./data/interim/
process_raw_data:
    python scripts/process-raw-data.py
```

I can now simply run `make process_raw_data` in the project's root directory.

#### Setting dependencies

Let's assume that the previous step (processing the raw data) generates new data inside `./data/interim/`. If now I have a second processing step that depends on the data generated by the previous step, I can set these data as dependencies for the new rule:

```make
## Process interim data
process_interim_data: $(wildcard data/interim/**/*)
    python scripts/process-interim-data.py
```

This way, the last step is only executed if the data it depends on has changed since the last time of execution.

For further information, have a look at Make's documentation: https://www.gnu.org/software/make/manual/html_node/Rules.html

#### Snakemake

Going one step further, in addition or as an alternative to `make`, [Snakemake](https://snakemake.readthedocs.io) provides even more extended functionalities.
Snakemake is pure Python, making it very convenient to work with and providing all the functionality of Python in your Snakemake workflow.
In Snakemake you define dependencies not as an "artificial" target but you indicate the target file you want to create, and Snakemake takes care of producing the required dependencies.
Another strength of Snakemake is that it is easily scalable:
Porting your Snakemake workflow from your local machine to a High-Performance Computing system is as straightforward as adding a few extra parameters to the executed command.
This way, Snakemake automatically generates bash scripts and submits them as jobs on the HPC, automatically distributing the tasks of the workflow.

### Document your project

The documentation of your project should include two kinds of documentation:

1. A documentation **of your code**, i.e. what it does, how to use it, and where to find the various functions –
similar to what you would expect when opening the online documentation of a Python package.
This should be considered as best practice and always be shipped with your code.
Most of this information you can and should indicate in the docstrings of your functions (you can even integrate short [tests as part of examples](https://docs.python.org/3/library/doctest.html)).
The rest can be written in normal Markdown or even Jupyter notebooks (see also the section below).
You also find some examples in the documentation shipped with this CookieCutter template.
2. A documentation **of your project**, i.e. a work log of what you did and why, what results you got etc.

#### What tool should I use?

##### For technical documentation

I personally recommend you to use [Jupyter-Book](https://jupyterbook.org/) (or [Sphinx](https://www.sphinx-doc.org/)) for the project documentation. Both of which are particularly suited for documenting Python code.
Sphinx is super feature-rich but also has a steep learning curve.
Jupyter-Book, on the other hand, is based on Sphinx and can therefore make use of all the complex features Sphinx provides, thereby being much easier to learn.
This is not least because you can write your content in Markdown or even integrate your Jupyter notebooks.
Also, with Sphinx's _autoapi_ extension (which can also be integrated in Jupyter-Book) you can parse the docstrings of your code and process them to nice HTML output.

> [!TIP]
> Describe as much of your code as possible in the docstrings of your functions, classes, and modules.
> Things should be as far as possible only described at one place and referenced at other occurrences.

> 📔 **Side note**<br>
> _Jupyter-Book_ can also be a nice way to share your collection of Jupyter notebooks online.
There are plugins that allow people to comment on the rendered HTML representation of your notebooks.

##### For scientific publications

In addition, you might want to write a scientific report or paper emerging from your project.
The standard therefore is LaTeX, I guess.
However, there are also alternatives that even integrate well with LaTeX and allow you to translate your documentation either into an interactive website or a static PDF.
Such an alternative is, for example [MyST-MD](https://mystmd.org/), which is more focussed on scientific publications in comparison to Jupyter-Book, which is more suited for technical documentations that include Jupyter notebooks.
To a certain extent, both are quite similar, though.

> [!IMPORTANT]
> Write your docstrings and code-related documentation alongside your code, i.e. in the same git branch you develop your code.
> For the scientific report/paper consider writing in a dedicated branch.

> [!TIP]
> Have a look at the "Guides to Better Science" from the British Ecological Society (see sources at the bottom).


#### Publish your documentation with [Github pages](https://pages.github.com/)

GitHub allows you to host static websites on its platform.
In this project template, I integrated a workflow for automatic deployment of your documentation (see the `.github/workflows/main.yml`).
The only thing you need to prepare is to go into your repository's settings (on Github), go to _Pages_ and then select "GitHub Actions" for _Source_. Save your changes. That's it.
Now, whenever you push something to the main branch, your documentation in `docs` will be automatically compiled and deployed. The result will be available on `https://<your-github-username>.github.io/<your-project-name>`. Magic… 🪄😉 

> [!NOTE]
> Keep in mind that the deployment may take a while. You can check the status of the workflow by clicking on "Action" in the menu bar of your repository.

### Some tips and thoughts regarding the code layout

#### High-level & low-level Code

All _high-level_ code (i.e. the code that the user is directly interacting with) should reside in the `scripts/` and the `notebooks/` directory.
High-level code is, for example, code that produces a figure, a report, or similar.\
Name scripts and notebooks in a way that indicates their order of execution (examples can be found in the respective directories).
It is also recommended to have _one_ script for each task, i.e. the creation of _one_ figure or _one_ table.

Code residing in `src/` is _exclusively_ source code or _low-level_ code and _is not meant to be actively run_ but rather used in your scripts and notebooks.


> ⚠️ **A note on version controlling Jupyter notebooks**<br>
It is very ugly to keep Jupyter Notebooks under version control as they are in principle a very large JSON file, containing lots of metadata, output of your cells, etc.
This circumstance makes it also quite hard to collaborate on them. 
However, there's help: _[Jupytext](https://jupytext.readthedocs.io/)_ syncs your Jupyter notebooks with another file for which you can choose a variety of formats (e.g. Markdown, R Markdown, normal Python, etc.).
These "paired" files, which can either reside alongside your Jupyter notebooks or in a separate directory, can then be easily version-controlled.
_Jupytext_ can either be used from the command line (`jupytext --sync notebooks/*ipynb`) or as a Jupyter plugin.
For more information, visit https://jupytext.readthedocs.io/.

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
    ├── docs               <- The technical documentation (default engine: Sphinx; but feel free to 
    │                         use MkDocs, Jupyter-Book or anything similar).
    │                         This should contain only documentation of the code and the assets.
    │                         A report of the actual project should be placed in `reports/book`.
    │
    ├── logs               <- Storage location for the log files being generated by scripts
    │
    ├── notebooks          <- Jupyter Notebooks. Follow a naming convention, such as a number (for ordering),
    │   │                     and a short `-` or `_` delimited description, e.g. `01-initial-analyses`
    │   ├── _paired        <- Optional location for your paired Jupyter Notebook files
    │   ├── exploratory    <- Notebooks for exploratory tasks
    │   └── reports        <- Notebooks generating reports and figures
    │
    ├── references         <- Data descriptions, manuals, and all other explanatory materials
    │
    ├── reports            <- Generated reports (e.g. HTML, PDF, LaTeX, etc.)
    │   ├── figures        <- Generated graphics and figures to be used in reporting
    │   └── README.md      <- More information about Jupyter-Book and MyST-MD
    │
    ├── scripts            <- High-level scripts that use (low-level) source code from `src/`
    ├── src                <- Source code (and only source code!) for use in this project
    │   ├── core           <- Provides some core functionalities
    │   ├── tests          <- Contains tests for the code in `src/`
    │   └── __init__.py    <- Makes src a Python module and provides some standard variables
    │
    ├── .env               <- In this file, specify all your custom environment variables
    │                         Keep this out of version control! (i.e. have it in your .gitignore)
    ├── .gitignore         <- Here, list all the files and folders (patterns allowed) that you want to
    │                         keep out of git version control.    
    ├── CHANGELOG.md       <- All major changes should go in there
    ├── CITATION.cff       <- The citation information for this project (update your ORCID ID!)
    ├── environment.yml    <- The conda environment file for reproducing the environment
    ├── LICENSE            <- The license used for this project
    ├── Makefile           <- A self-documenting Makefile for standard CLI tasks
    ├── pyproject.toml     <- Configuration file for the project
    ├── README.md          <- The top-level README of this project
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`

## Dummy files

The following files are for demonstration purposes only and, if not needed, can be deleted safely:

    ├── notebooks/01-minimal-example.ipynb
    ├── docs/*
    ├── reports/book/*
    ├── scripts/01-test.py
    └── src
        ├── tests/*
        └── submodule.py

## Sources of inspiration

Some great sources of inspiration and orientation when I created this template:

- A great article on how to structure your scientific data projects: https://drivendata.github.io/cookiecutter-data-science
- https://coderefinery.github.io/reproducible-research/
- https://github.com/drivendata/cookiecutter-data-science
- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://github.com/hackalog/easydata
- https://github.com/aubricus/cookiecutter-python-package
- Martin, R. C. (Ed.). (2009). Clean code: A handbook of agile software craftsmanship. Prentice Hall.
- Croucher, M., Graham, L., James, T., Krystalli, A., & Michonneau, F. (2019). Reproducible Code (Guides to Better Science). British Ecological Society. https://www.britishecologicalsociety.org/publications/guides-to/

## Contributing

Issues & pull requests accepted.

***

&copy; [Markus Ritschel](https://github.com/markusritschel), 2021–2024
