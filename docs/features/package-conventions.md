---
icon: material/toolbox-outline
---

# Package Conventions

Beyond the tooling, the generated package ships with a small set of conventions and helpers that the
example scripts and notebooks already rely on. They exist to solve three recurring annoyances in
research code: paths that break when a script moves, logs that vanish, and output files nobody can
trace back to the code that produced them.

Everything below lives in `src/mypackage/` and is importable as soon as you `import mypackage`.

## Path variables

Resolving paths relative to the _file you happen to be in_ is the single most common source of
breakage when a script moves or a notebook is run from a different directory. The package resolves
them once, relative to the project root, and exports them:

| Variable   | Points to          | Available when    |
| ---------- | ------------------ | ----------------- |
| `BASE_DIR` | the project root   | always            |
| `LOG_DIR`  | `logs/`            | always            |
| `DATA_DIR` | `data/`            | research projects |
| `PLOT_DIR` | `reports/figures/` | research projects |

`BASE_DIR` is derived from the package's own location (`Path(__file__).resolve().parents[2]`), so it
is correct no matter where the calling code sits.

```python
from mypackage import DATA_DIR, PLOT_DIR

df = pd.read_csv(DATA_DIR / "raw" / "input.csv")
fig.savefig(PLOT_DIR / "result.png")
```

!!! tip
    Use them everywhere instead of `../..` chains or `os.getcwd()`. A notebook in
    `notebooks/exploratory/` and a script in `scripts/` then reference the same file by the same
    expression.

## Environment variables

`.env` in the project root is loaded automatically at import time via
[python-dotenv](https://pypi.org/project/python-dotenv/) — the package calls `find_dotenv()`, which
walks up the directory tree, so it is found from subdirectories too.

Put machine-specific settings, credentials and paths there:

```bash title=".env"
LOGLEVEL=DEBUG
MY_API_TOKEN=...
```

!!! warning "`.env` is git-ignored on purpose"
    It is meant for values that must not be committed. If a variable is needed to _run_ the project,
    document its name and meaning in the README — never its value.

`LOGLEVEL` is read by the logging helper below and defaults to `INFO`.

## Logging

`setup_logger()` configures a logger with two handlers in one call — a stream handler for the
terminal and a file handler writing into `LOG_DIR`:

```python
from mypackage import setup_logger

log = setup_logger()          # level from $LOGLEVEL, log file named after the calling script
log.info("Processing started")
```

| Argument  | Effect                                                                                 |
| --------- | -------------------------------------------------------------------------------------- |
| `level`   | Log level; defaults to `$LOGLEVEL`, else `INFO`                                        |
| `logfile` | `True` → `LOG_DIR/<calling-script>_<pid>.log`; a string → that path; `False` → no file |
| `name`    | Logger name                                                                            |

The log file name includes the calling script's stem and the process ID, so parallel runs of the
same script do not overwrite each other's logs. Records are formatted with a timestamp, level,
module and line number.

!!! note "The file handler is always at DEBUG"
    The root logger is set to `DEBUG` so the _file_ captures everything, while the level you pass
    governs what reaches the terminal. Turning the console quiet therefore does not cost you detail
    in the log.

!!! tip
    `logs/` is generated for every project. [`lnav`](https://lnav.org/) is a comfortable way to read
    the files.

## `save()` — one call, with provenance

`core/utils.py` provides a [`functools.singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch)
`save()` that dispatches on the type of the object you hand it:

| Object type                | Dispatches to    |
| -------------------------- | ---------------- |
| `matplotlib.figure.Figure` | `fig.savefig()`  |
| `pandas.DataFrame`         | `df.to_csv()`    |
| `xarray.Dataset`           | `ds.to_netcdf()` |

Any other type raises `NotImplementedError` telling you to use the object's native method.

```python
from mypackage import save

save(fig, PLOT_DIR / "timeseries.png", dpi=175)
save(ds, DATA_DIR / "processed" / "gridded.nc")
```

Extra keyword arguments are forwarded to the underlying method, so `dpi=`, `index=False` and friends
work as usual.

### The provenance decorator

The reason to prefer `save()` over `fig.savefig()` is the `@add_metadata` decorator wrapped around
it. On every call it:

1. resolves the **short git commit hash** of the working tree,
2. appends it to the filename — `timeseries.png` becomes `timeseries_a1b2c3d.png`,
3. records the calling file and line number, and logs all of it,
4. for figures, additionally embeds the metadata into the image file itself.

Months later, a figure in a manuscript can be traced back to the exact commit and line that produced
it. Pass `add_hash=False` to opt out for a single call:

```python
save(fig, PLOT_DIR / "for-publication.png", add_hash=False)
```

!!! warning "Requires a git repository"
    The hash is obtained by shelling out to `git rev-parse`. The template initializes a repository
    during generation, so this holds by default — but `save()` will fail if you run it somewhere
    without git history.

## Matplotlib style sheets

`assets/mpl_styles/` contains two starting-point style sheets — `white_paper.mplstyle` for
publications and `dark_presentation.mplstyle` for talks. Apply one at the top of a plotting script
so all figures come out consistent:

```python
from mypackage import BASE_DIR
import matplotlib.pyplot as plt

plt.style.use(BASE_DIR / "assets/mpl_styles/white_paper.mplstyle")
```

See the [Matplotlib documentation](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
on customizing, and its [built-in style reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
for alternatives.

## Where to put code

The `src/` layout is deliberate: tests and scripts run against the _installed_ package rather than
loose files next to them, which catches missing dependencies and broken imports that a flat layout
would hide.

That gives a clear split:

- **`src/mypackage/`** — low-level, reusable code. Not meant to be executed directly.
- **`scripts/` and `notebooks/`** — high-level code you actually run, which imports from the package.

When a function in a notebook proves itself, move it into the package and import it back. See
[Research Projects](./research-projects.md) for the full workflow.

## See Also

- [Research Projects](./research-projects.md) — the data-science directory structure
- [Code Quality](./code-quality.md) — how docstrings in `src/` become tests
- [Development](./development.md) — the day-to-day workflow
