---
icon: material/console-line
---

# Command-Line Interface

The `command_line_interface` [prompt](../prompts.md#tool-choices) can scaffold a CLI for your
package. It defaults to **No command-line interface** — choose one deliberately if you want your
package to be runnable as a command.

| Choice                      | Library                                     | Style                                     |
| --------------------------- | ------------------------------------------- | ----------------------------------------- |
| `Typer`                     | [Typer](https://typer.tiangolo.com/)        | Type hints become the argument parser     |
| `Click`                     | [Click](https://click.palletsprojects.com/) | Decorator-based, mature, very widely used |
| `Docopt`                    | [docopt](http://docopt.org/)                | The module docstring _is_ the parser      |
| `No command-line interface` | —                                           | No `cli.py`, no entry point               |

If you are undecided, take Typer: it derives the interface from the annotations you should be
writing anyway, and the type hints stay useful to `ty` and to readers.

!!! note "Nothing is generated for the default"
    With "No command-line interface" there is no `cli.py` and no `[project.scripts]` section. You can
    add one later by hand, or re-run `copier update` with a changed answer.

## What gets generated

Choosing any of the three libraries produces `src/mypackage/cli.py` with a placeholder command that
prints a banner, plus an entry point in `pyproject.toml`:

```toml title="pyproject.toml"
[project.scripts]
my-project = "mypackage.cli:app"
```

The command is named after your `project_slug`, while the module path uses `package_name`. **All
three flavours expose the entry point as `app`**, so the `[project.scripts]` line is identical
regardless of which you picked — only the body of `cli.py` differs.

Because `uv sync` installs your project, the command is available in the environment immediately:

```bash
uv run my-project          # or just `my-project` with the venv activated
```

`cli.py` also has an `if __name__ == "__main__":` guard, so `uv run python -m mypackage.cli` works
during development.

## Replacing the placeholder

=== "Typer"

    ```python title="src/mypackage/cli.py"
    import typer
    from rich.console import Console

    app = typer.Typer()
    console = Console()


    @app.command()
    def main(name: str, count: int = 1):
        """Greet someone."""
        for _ in range(count):
            console.print(f"Hello {name}")
    ```

    Parameter types come from the annotations: `name` becomes a required argument and `count` an
    optional `--count` option with a default. Add more subcommands by decorating further functions
    with `@app.command()`.

=== "Click"

    ```python title="src/mypackage/cli.py"
    import click
    from rich.console import Console

    console = Console()


    @click.command()
    @click.argument("name")
    @click.option("--count", default=1, help="Number of greetings.")
    def app(name, count):
        """Greet someone."""
        for _ in range(count):
            console.print(f"Hello {name}")
    ```

    Note that the function itself is named `app` here — it is the object the entry point resolves
    to. For multiple subcommands, turn it into a `@click.group()` and attach commands to it.

=== "Docopt"

    ```python title="src/mypackage/cli.py"
    """my-project.

    Usage:
      my-project <name> [--count=<n>]
      my-project (-h | --help)

    Options:
      -h --help       Show this message.
      --count=<n>     Number of greetings [default: 1].
    """

    from docopt import docopt
    from rich.console import Console

    console = Console()


    def app():
        """Greet someone."""
        args = docopt(__doc__)
        for _ in range(int(args["--count"])):
            console.print(f"Hello {args['<name>']}")
    ```

    !!! warning "The docstring is the interface"
        docopt parses the module docstring at runtime to build the parser. If you add an option to
        the code without adding it to the `Usage:` block, it simply will not exist. Keep the two in
        sync — this is the trade-off for the approach's brevity.

## Linting

`ruff.toml` exempts CLI modules from the docstring rules that add little value there:

```toml title="ruff.toml"
[lint.per-file-ignores]
"**/cli.py"      = ["D101", "D102", "D103"]
"**/__main__.py" = ["D"]
```

`B008` (function calls in argument defaults) is also disabled globally, because it is the normal
idiom in Typer and Click for declaring options.

## See Also

- [Task Automation](./justfile.md) — wrapping long invocations in `just` recipes
- [Publishing](./publish-package.md) — shipping your command to PyPI
- [Prompts](../prompts.md) — the full prompt reference
