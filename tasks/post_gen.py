"""Post-generation task for the Copier template.

Runs in the freshly generated project directory (Copier sets the CWD to the
destination). Only invoked on first `copier copy`, never on `copier update`
(guarded by `when: _copier_operation == 'copy'` in copier.yml). Replaces the
inline POSIX-shell `_tasks` entries previously in copier.yml, which required
a POSIX shell (WSL/git-bash on Windows) to run at all: git init + first
commit, `uv sync --dev`, and pre-commit setup.

Usage: post_gen.py <package_name>
"""

import shutil
import subprocess
import sys

package_name = sys.argv[1] if len(sys.argv) > 1 else ""

# Example/boilerplate files that should be present but left uncommitted, so the
# user replaces them with their own code instead of inheriting them as history.
example_files = [
    "notebooks/*.ipynb",
    "scripts/*.py",
    f"src/{package_name}/cli.py",
    f"src/{package_name}/submodule.py",
    "tests/*.py",
]

if shutil.which("git"):
    print("Initialize Git repository and make a first commit")
    subprocess.run(["git", "init", "-q"], check=True)
    subprocess.run(["git", "branch", "-m", "main"], check=True)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(
        ["git", "rm", "--cached", "-q", "--ignore-unmatch", *example_files], check=True
    )
    subprocess.run(
        [
            "git",
            "commit",
            "-q",
            "-m",
            (
                "Set up new project from copier template "
                "https://github.com/markusritschel/cookiecutter-pyproject"
            ),
        ],
        check=True,
    )

    if shutil.which("uv"):
        print("Install development dependencies and set up pre-commit hooks")
        subprocess.run(["uv", "sync", "--dev"], check=True)
        subprocess.run(["uv", "run", "pre-commit", "install"], check=True)
        subprocess.run(["git", "add", "uv.lock", "pyproject.toml"], check=True)
        subprocess.run(
            [
                "git",
                "commit",
                "-q",
                "-m",
                "Set up pre-commit hooks and install dev dependencies",
            ],
            check=True,
        )
    else:
        print("WARNING: 'uv' not found. Run the following manually after installation:")
        print("  uv sync --dev")
        print("  uv run pre-commit install")
else:
    print("WARNING: 'git' not found. Initialize the repository manually:")
    print(
        "  git init && git branch -m main && git add . && git commit -m 'Initial commit'"
    )
