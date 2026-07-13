# !/usr/bin/env python3
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.project_author }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
from {{ cookiecutter.package_name }}.submodule import generate_int_list


def test_subfunc(global_fixture):
    list_example = generate_int_list()
    assert isinstance(list_example, list)
    assert isinstance(global_fixture, str)
