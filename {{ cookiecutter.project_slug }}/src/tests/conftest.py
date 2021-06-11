#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.full_name }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
import pytest


@pytest.fixture
def global_fixture(request):
    return 'Test'
