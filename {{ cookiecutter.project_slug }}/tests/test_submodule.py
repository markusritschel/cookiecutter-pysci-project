# !/usr/bin/env python3
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.project_author }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
import pytest # noqa: F401 # suppress unused-import error, as it actually needed here to work with pytest
from {{ cookiecutter.package_name }}.submodule import generate_int_list

def test_subfunc(global_fixture):
    list_example = generate_int_list()
    assert isinstance(list_example, list)
    assert isinstance(global_fixture, str)
