# Examples

## Citations & Bibliography

This is to demonstrate the bibliography feature.
We cite a few entries from the `references.bib` file, such as {cite}`doe_sphinx_2026` (``{cite}`doe_sphinx_2026` ``).
You can also use in-text citations {cite:t}`doe_sphinx_2026` (using `{cite:t}`) or use the exlicite `{cite:p}` directive, which puts the reference in brackets {cite:p}`doe_sphinx_2026`.

You can hover the links to see the details, and a click will bring you to the [bibliography](bibliography.md).


## Code blocks

```python
def hello_world():
    print("Hello, world!")
```


## Math

You can even use $\LaTeX$ to write math blocks, either by using the standard math block syntax

```latex
$$
\begin{equation*}
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
\end{equation*}
$$
```
$$
\begin{equation*}
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
\end{equation*}
$$

or by using the `{math}` directive, which allows you to label your equations and reference them later on.

````rst

```{math}
:label: my-math-ref
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```
````
```{math}
:label: my-math-ref
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```

which you can even reference in your text (see Equation {eq}`my-math-ref`).

## Link to API

You can even link to objects in your code, either by referencing them by their actual member
{py:obj}`{{ cookiecutter.project_slug }}.core.utils`
or, by using an 
{py:obj}`alias <{{ cookiecutter.project_slug }}.core.utils.save>`
.
You can also reference code of external libraries, such as {py:obj}`numpy.ndarray` or {class}`xarray.Dataset`. They are automatically linked to their respective documentation, so you can easily check the details of the API.
