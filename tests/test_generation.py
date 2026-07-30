"""Generation tests for the template itself.

These render the template from the *working tree* and assert on the resulting
file tree. They exist because the CI pipeline cannot catch a dropped file: it
runs `pytest` in the generated project, which exits 0 on the doctests in
`core/utils.py` even when `tests/` is empty and the example modules are missing.

Rendering goes through a plain (non-git) copy of the repository so that copier
takes its filesystem path rather than its VCS path. That renders exactly what is
on disk — uncommitted changes included — and avoids `--vcs-ref` resolving to the
latest git tag.
"""

import re
import shutil
from pathlib import Path

import pytest
from copier import run_copy

REPO_ROOT = Path(__file__).resolve().parents[1]

# Directories that must not be handed to copier as part of the template source.
IGNORED = shutil.ignore_patterns(
    ".git",
    ".venv",
    ".remember",
    "site",
    ".cache",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
)

# Real dotfiles, as opposed to a filename whose Jinja-conditional stem rendered
# to the empty string (e.g. `.ipynb`, `.md`) — see test_no_filename_lost_its_stem.
KNOWN_DOTFILES = {
    ".env",
    ".gitignore",
    ".gitkeep",
    ".gitattributes",
    ".copier-answers.yml",
}

BARE_EXTENSION = re.compile(r"^\.[a-z]+$")


@pytest.fixture(scope="session")
def template_src(tmp_path_factory):
    """A plain-directory copy of the template repository."""
    src = tmp_path_factory.mktemp("template_src") / "template-repo"
    shutil.copytree(REPO_ROOT, src, ignore=IGNORED)
    return src


def _generate(template_src, dst, **answers):
    run_copy(
        str(template_src),
        str(dst),
        data={"project_name": "Python Boilerplate", **answers},
        defaults=True,
        unsafe=True,  # the template declares _tasks and a jinja extension
        skip_tasks=True,  # git init / uv sync are not under test here
        quiet=True,
    )
    return dst


@pytest.fixture(scope="session")
def research_project(template_src, tmp_path_factory):
    dst = tmp_path_factory.mktemp("research") / "proj"
    return _generate(template_src, dst, is_research_project=True)


@pytest.fixture(scope="session")
def library_project(template_src, tmp_path_factory):
    dst = tmp_path_factory.mktemp("library") / "proj"
    return _generate(template_src, dst, is_research_project=False)


# Example/boilerplate files a freshly generated project must contain. Keep in
# sync with `example_files` in tasks/post_gen.py, which un-stages them.
COMMON_EXAMPLE_FILES = [
    "docs/example.md",
    "src/python_boilerplate/submodule.py",
    "src/python_boilerplate/cli.py",
    "tests/conftest.py",
    "tests/test_submodule.py",
]
RESEARCH_EXAMPLE_FILES = [
    "notebooks/01-minimal-example.ipynb",
    "scripts/01-test.py",
]


@pytest.mark.parametrize("relpath", COMMON_EXAMPLE_FILES + RESEARCH_EXAMPLE_FILES)
def test_research_project_has_example_file(research_project, relpath):
    assert (research_project / relpath).is_file()


@pytest.mark.parametrize("relpath", COMMON_EXAMPLE_FILES)
def test_library_project_has_example_file(library_project, relpath):
    assert (library_project / relpath).is_file()


def test_cli_defines_a_command(research_project):
    """A Typer app with no command raises when the entry point is invoked."""
    cli = (research_project / "src/python_boilerplate/cli.py").read_text()
    assert "@app.command()" in cli


def test_example_script_imports_a_module_that_exists(research_project):
    """`scripts/01-test.py` imports submodule.py; both must ship together."""
    assert (research_project / "src/python_boilerplate/submodule.py").is_file()
    script = (research_project / "scripts/01-test.py").read_text()
    assert "from python_boilerplate.submodule import" in script


def test_no_filename_lost_its_stem(research_project):
    """Catch a Jinja-conditional filename whose condition rendered falsy.

    An undefined variable in a path condition yields an empty stem, leaving a
    bare extension like `.ipynb` instead of dropping the file loudly.
    """
    lost = [
        p.relative_to(research_project)
        for p in research_project.rglob("*")
        if p.is_file() and p.name not in KNOWN_DOTFILES and BARE_EXTENSION.match(p.name)
    ]
    assert not lost, f"filenames rendered to a bare extension: {lost}"


def test_no_unrendered_jinja_in_filenames(research_project):
    leftover = [
        p.relative_to(research_project)
        for p in research_project.rglob("*")
        if "{%" in p.name or "{{" in p.name
    ]
    assert not leftover, f"unrendered Jinja in filenames: {leftover}"


def test_tests_directory_is_not_empty(research_project):
    assert list((research_project / "tests").glob("test_*.py"))


def test_research_directories_are_conditional(research_project, library_project):
    for relpath in ("data", "notebooks", "references", "reports", "scripts"):
        assert (research_project / relpath).is_dir()
        assert not (library_project / relpath).exists()
