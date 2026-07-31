---
icon: material/book-open-variant
---

# Documentation

Every generated project ships with a documentation setup. Which one you get depends on your answer
to the `docs_engine` [prompt](../prompts.md#tool-choices) — **Sphinx**, **Zensical** or **MyST** —
and that answer determines the contents of `docs/`, the `docs` dependency group, the commands behind
`just docs`, and the generated GitHub Actions workflow.

Once GitHub Pages is configured in your repository settings, the documentation is deployed
automatically on every push to `main`[^1].

[^1]: See [GitHub Actions](./github-actions.md) for the workflow details and the one-time Pages setup.

## Choosing an engine

If you are unsure, take the default. Sphinx is the only option that gives you API documentation
generated from your docstrings, which is usually the deciding factor for a package.

|                          | **Sphinx** _(default)_            | **Zensical**                    | **MyST**                         |
| ------------------------ | --------------------------------- | ------------------------------- | -------------------------------- |
| Best for                 | Python packages with a public API | Handbooks, project sites        | Papers, computational narratives |
| API docs from docstrings | ✅ `sphinx-autoapi`               | ❌                              | ❌                               |
| Citations / BibTeX       | ✅ `sphinxcontrib-bibtex`         | ❌                              | ✅ native                        |
| Markdown flavour         | MyST (via `myst-parser`)          | Python-Markdown + extensions    | MyST                             |
| Configuration            | `docs/conf.py` + `docs/_config/`  | `zensical.toml` (project root)  | `docs/myst.yml`                  |
| Navigation               | `toctree` in `index.md`           | derived from the directory tree | `toc:` in `myst.yml`             |
| Build output             | `docs/_build/html/`               | `site/`                         | `docs/_build/html/`              |
| `docs` dependency group  | ~26 packages                      | 1 package                       | 1 package                        |

!!! warning "The choice is not easily reversible"
    `docs_engine` decides which files are generated, so switching later means running
    `copier update` with a changed answer and reconciling the result by hand. The Markdown you write
    mostly carries over; the configuration and any engine-specific directives do not.

## Building the documentation

Identical for all three engines:

```bash
just docs          # Build the documentation
just docs-serve    # Serve with live reload (http://localhost:8000)
```

The `docs/` directory ships with a few Markdown files to get you started — an `index.md`, an
`example.md` demonstrating the engine's features, and stubs for the README, license and
bibliography. Start editing them and add new ones as you go.

!!! note "`just clean-docs` is Sphinx-shaped"
    It removes `docs/_build/` and `docs/api/`. Under Zensical the build output is `site/`, so remove
    that directory instead (it is already git-ignored).

## Engine reference

=== "Sphinx"

    [Sphinx](https://www.sphinx-doc.org/) is the classic Python documentation generator. The
    template configures it so you can write almost everything in Markdown via the
    [MyST parser](https://myst-parser.readthedocs.io/) — no reStructuredText required.

    ### Configuration

    `docs/conf.py` holds the essentials and then composes the rest from `docs/_config/`, one module
    per concern:

    | Module | What it configures |
    | --- | --- |
    | `autoapi.py` | API documentation generated from your source |
    | `bibtex.py` | Citation support |
    | `images.py` | Figure and image handling |
    | `intersphinx.py` | Cross-links to external documentation |
    | `myst.py` | Markdown parsing and extensions |
    | `napoleon.py` | NumPy/Google docstring parsing |
    | `typehints.py` | Rendering of type annotations |
    | `themes/*.py` | Per-theme options (`furo`, `sphinx_immaterial`) |

    Switch themes with the `html_theme` variable in `conf.py` — `furo` is the default, and
    `sphinx_rtd_theme`, `pydata_sphinx_theme`, `sphinx_book_theme` and `sphinx_immaterial` are all
    installed. Theme-specific options live in `docs/_config/themes/<theme_name>.py`; if a matching
    module does not exist, `conf.py` prints a warning and carries on with the theme defaults.

    !!! tip
        Run `just clean-docs` after changing the theme, before rebuilding.

    ### Navigation

    Sphinx needs an explicit table of contents. Define it in `index.md` with a `toctree`, hidden if
    you want it in the sidebar only:

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

    Pages are listed without the `.md` extension. A Markdown file that is not in any `toctree` is
    built but unreachable, and Sphinx will warn about it.

    ### API documentation from docstrings

    Write self-explanatory docstrings and `sphinx-autoapi` extracts them automatically — no stub
    files to maintain. They are rendered wherever you add `api/index` to a `toctree`.

    ```python title="src/mypackage/example.py"
    def user_data(name: str, age: int) -> dict:
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

    !!! info "Docstrings are also tests"
        `--doctest-modules` is enabled, so any `>>>` example in these docstrings runs under pytest.
        See [Doctests](./code-quality.md#doctests-your-docstrings-are-tests).

    ### Citations

    Curate `docs/references.bib` (ideally exported from Zotero) and cite with ``{cite}`yourCitekey` ``.
    The `{cite:t}` and `{cite:p}` roles give you in-text and parenthetical forms. The rendered list
    lives in `bibliography.md`.

    ### Cross-references

    `intersphinx` links your documentation to external projects and to your own API. Add lookup
    tables for further packages via `intersphinx_mapping` in `docs/_config/intersphinx.py`. This is
    what makes `{py:obj}`, `{class}` and friends in `example.md` resolve to real pages.

    ### Further reading

    - [Sphinx documentation](https://www.sphinx-doc.org/)
    - [MyST parser guide](https://myst-parser.readthedocs.io/)
    - [Sphinx themes](https://www.sphinx-doc.org/en/master/usage/theming/)

=== "Zensical"

    [Zensical](https://zensical.org/) is the successor to Material for MkDocs, from the same
    authors. It is the fastest of the three and produces the most polished default site — the
    documentation you are reading right now is built with it.

    ### Configuration

    Everything lives in a single `zensical.toml` at the **project root** (not in `docs/`). The
    generated file is heavily commented and sets up:

    - a light/dark palette toggle,
    - code copy/annotate/select buttons, footnote tooltips and linked content tabs,
    - instant navigation with prefetching, breadcrumbs and a back-to-top button.

    Uncomment what you want; each option links to the relevant page of the Zensical documentation.

    ### Navigation

    By default the navigation is derived from the directory structure of `docs/`, so a new Markdown
    file simply appears. To control the order and grouping, define `nav` explicitly:

    ```toml title="zensical.toml"
    [project]
    nav = [
      {"Home" = "index.md"},
      "tutorial.md",
      {"Features" = [
        "features/development.md",
        "features/uv.md",
      ]},
    ]
    ```

    !!! warning "Once `nav` exists, it is exhaustive"
        An unlisted page is still built and reachable by URL, but appears in no menu. Add each new
        page to `nav` as you create it.

    ### What you don't get

    - **No API documentation.** Nothing generates pages from your docstrings. If you want it,
      add and configure [mkdocstrings](https://mkdocstrings.github.io/) yourself.
    - **No BibTeX support**, which is why no `references.bib` or `bibliography.md` is generated for
      Zensical. If you need citations, Sphinx or MyST is the better choice.
    - The `readme.md` and `license.md` stubs are not generated either — they rely on a Sphinx
      `{include}` directive that Python-Markdown does not understand. Link to the files on GitHub
      instead, or paste the content in.

    ### Further reading

    - [Zensical documentation](https://zensical.org/docs/)
    - [Material for MkDocs reference](https://squidfunk.github.io/mkdocs-material/reference/) (most authoring syntax carries over)

=== "MyST"

    [MyST-MD](https://mystmd.org/) is a Markdown-first engine aimed at scientific and technical
    writing. Despite the shared name it is **not** Sphinx with a Markdown parser — it is a separate
    toolchain (`mystmd`) with its own build pipeline, structured around papers, cross-references and
    executable content.

    ### Configuration

    `docs/myst.yml` holds project metadata (title, description, authors, GitHub URL), the
    bibliography, the table of contents and the site template. The generated file uses the
    `book-theme`.

    ### Navigation

    Explicit, as a `toc:` list in `myst.yml`:

    ```yaml title="docs/myst.yml"
    project:
      toc:
        - file: index.md
        - file: example.md
        - file: bibliography.md
    ```

    ### Citations

    Native and configured out of the box — `bibliography: [references.bib]` in `myst.yml` — so
    ``{cite}`yourCitekey` `` works without extra extensions.

    ### What you don't get

    - **No API documentation.** `mystmd` has no autodoc equivalent, so your docstrings are not
      rendered anywhere, and `{py:obj}`-style cross-references into your own code have no inventory
      to resolve against. Document your API by hand, or choose Sphinx.
    - References are rendered per page wherever you cite, so the generated `bibliography.md` is a
      landing page rather than a generated list. Keep it for citation notes or delete it.

    ### Further reading

    - [MyST-MD guide](https://mystmd.org/guide)
    - [MyST website options](https://mystmd.org/guide/website)

## Writing Markdown

Regardless of engine, keep the documentation next to the code and update it in the same commit.
Sphinx and MyST both use [MyST Markdown](https://mystmd.org/guide/typography), so directives are
written as fenced blocks:

````md
```{note}
This renders as an admonition in Sphinx and MyST.
```
````

Zensical instead uses the Python-Markdown convention:

```md
!!! note
    This renders as an admonition in Zensical.
    ```

This is the main source of friction if you ever switch engines — prose carries over unchanged,
directives do not.
