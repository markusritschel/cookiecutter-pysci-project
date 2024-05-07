![](_static/logo.png)

## Introduction

Welcome to the documentation of {{ cookiecutter.project_name }}!

{{ cookiecutter.project_description }}

```{tip}
- Give a short introduction on what the project is about.
- Limit yourself to just a few sentences.
- Mention any preknowledge the user must have for the project.
- You may also give some instructions on how to navigate through the documentation.
```

## Getting Started

### Installation

For getting started in the fastest way possible, there are *Make* targets provided.
To set up the project, simply run the following commands from the main directory:

First, run

```bash
make conda-env
# or alternatively
make install-requirements
```

to install the required packages either via `conda` or `pip`, followed by

```bash
make src-available
```

to make the project's routines (located in `src`) available for import.

### Test code

You can run

```bash
make tests
```

to run the tests via `pytest`.

### Make data available

You may need to make data available under `data`.
These can be either copied directly into the directory or, if the files are too big and/or already reside somewhere your machine can access it directly, create links in `data`, pointing to the actual location of the data.

You should now be set to proceed with executing the scripts and notebooks. 🚀

## Data

```{tip}
Describe the data you use in the project.
```

## Workflow

```{tip}
Describe the workflow that should be followed to reproduce the results of your project.
```


## Contact

For any questions or issues, please contact me via {{ cookiecutter.email }} or open an [issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues).
