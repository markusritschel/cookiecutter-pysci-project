"""CLI script for {{ cookiecutter.package_name }}."""

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """CLI script for {{ cookiecutter.package_name }}."""
    console.print("Replace this message by putting your code into "
               "{{ cookiecutter.package_name }}.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")


if __name__ == "__main__":
    app()
