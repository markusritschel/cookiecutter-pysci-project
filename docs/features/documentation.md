---
icon: material/book-open-variant
---

# Documentation

Generate professional documentation from Markdown and Python code using [Sphinx](https://www.sphinx-doc.org/). 
Once configured in your GitHub repository settings, your documentation is automatically deployed to GitHub Pages via GitHub Actions [^1].

[^1]: Also see [Github Actions](./github-actions.md)


## Building Documentation

```bash
just docs          # Build HTML documentation
just docs-serve    # Serve with live reload (http://localhost:8000)
```

The `docs` directory holds a few Markdown files to get you started.
Just start editing them and add new ones according to your needs.


## Configuration

In the `_config` subdirectory there are configuration files for various plugins/extensions for a more sophisticated rendering of your documentation.
Customize theme-specific settings in `docs/_config/themes/<theme_name>.py`.
You can specify another theme in the `html_theme` variable inside the `conf.py` file in the `docs` directory. 
If you change the theme, please run a `just clean-docs` before you build them again.


## Writing Documentation

### Markdown files
The `myst` extension enables you to write your documentation almost entirely in Markdown. 
No need for complicated rst syntax.
Just place your Markdown files in the `docs/` directory.

In your `index.md`, specify the table of contents (`toctree`) to define the structure of the documentation:
````md
```{toctree}
:hidden:
:caption: Main navigation

example
demo-stuff
api/index
bibliography
```
````


### Python docstrings
Add self-explanatory docstrings to your functions.
The `autoapi` extensions extracts them automatically and renders them if `api/index` is added to your `toctree` (see above).

```python title="./src/your-package/example.py"
def process_data(name: str, age: int) -> dict:
    """Process user data.
    
    Parameters
    ----------
    name : str
        User's full name
    age : int
        User's age in years
    """
    return {name: age}
```

### Citations
The `bibtex` extension enables you to add citations to your documentation. 
Curate your `references.bib` file (ideally export it from Zotero), and cite with ``{cite}`yourCitekey` ``.

### Intersphinx
The `intersphinx` extension enables you to create links between your documentation and external documentation (i.e. documentation from external packages) as well as your own code base.
Have a look at the files for examples.
You can add look-up tables for various packages by modifying the `intersphinx_mapping` variable in the `docs/_config/intersphinx.py`.


## Further Reading

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Parser Guide](https://myst-parser.readthedocs.io/)
- [Sphinx Themes](https://www.sphinx-doc.org/en/master/usage/theming/)
