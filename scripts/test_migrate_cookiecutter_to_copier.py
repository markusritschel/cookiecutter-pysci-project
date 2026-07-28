import json

import pytest
import yaml
from migrate_cookiecutter_to_copier import (
    build_answers_file,
    load_cruft_context,
    map_to_copier_answers,
)

CRUFT_CONTEXT = {
    "project_author": "Markus Ritschel",
    "email": "git@markusritschel.de",
    "github_username": "markusritschel",
    "project_name": "My Code Base",
    "project_slug": "my-code-base",
    "package_name": "my_code_base",
    "is_research_project": False,
    "_copy_without_render": [".github/workflows/*"],
    "_template": "https://github.com/markusritschel/cookiecutter-pyproject",
    "_commit": "ce5a67c9a1bfc0eb10ab0b6200757f0371605b1d",
}


def test_load_cruft_context_drops_underscore_keys(tmp_path):
    cruft_json = tmp_path / ".cruft.json"
    cruft_json.write_text(json.dumps({"context": {"cookiecutter": CRUFT_CONTEXT}}))

    context = load_cruft_context(cruft_json)

    assert not any(key.startswith("_") for key in context)
    assert context["project_author"] == "Markus Ritschel"


def test_load_cruft_context_rejects_wrong_shape(tmp_path):
    cruft_json = tmp_path / ".cruft.json"
    cruft_json.write_text(json.dumps({"not_context": {}}))

    with pytest.raises(SystemExit):
        load_cruft_context(cruft_json)


def test_map_to_copier_answers_renames_known_keys_and_passes_through_rest():
    context = {k: v for k, v in CRUFT_CONTEXT.items() if not k.startswith("_")}

    answers = map_to_copier_answers(context)

    assert answers["user_name"] == "Markus Ritschel"
    assert answers["user_email"] == "git@markusritschel.de"
    assert answers["github_user"] == "markusritschel"
    assert "project_author" not in answers
    assert "email" not in answers
    assert "github_username" not in answers
    assert answers["project_slug"] == "my-code-base"
    assert answers["package_name"] == "my_code_base"
    assert answers["is_research_project"] is False


def test_build_answers_file_leads_with_commit_and_src_path():
    content = build_answers_file(
        {"user_name": "Markus Ritschel"},
        "abc123",
        "gh:markusritschel/cookiecutter-pyproject",
    )

    parsed = yaml.safe_load(content)
    assert parsed["_commit"] == "abc123"
    assert parsed["_src_path"] == "gh:markusritschel/cookiecutter-pyproject"
    assert parsed["user_name"] == "Markus Ritschel"
    keys = list(parsed.keys())
    assert keys[:2] == ["_commit", "_src_path"]
