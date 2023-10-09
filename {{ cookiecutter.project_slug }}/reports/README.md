# Important hint

For written reports resulting from your project, you may consider using MyST-MD rather than Jupyter-Book or Sphinx as this will not be a mere technical documentation of your project but rather a report or paper-alike document.

Follow the instructions on https://mystmd.org/ to create your website version of this report or export it to PDF or LaTeX.

You may delete this README ;-)

## Start with sample projects

### Jupyter-Book

From the root of the project, execute

```bash
jupyter-book create reports/jbook
jupyter-book build reports/jbook
```

More info [here](https://jupyterbook.org/en/stable/start/create.html).

### MyST-MD

From the root of the project, execute

```bash
git clone https://github.com/executablebooks/mystmd-quickstart.git reports/myst-article
cd reports/myst-article
myst init
```

👉 More info [here](https://mystmd.org/guide/quickstart-myst-websites).

***

> [!NOTE]
> Feel free to choose a different path (it's recommended though to place it in `reports`).
