# !/usr/bin/env python3
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.project_author }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
import pytest
from src import submodule

def test_subfunc(global_fixture):
    l = submodule.generate_int_list()
    assert isinstance(l, list)
    assert isinstance(global_fixture, str)
