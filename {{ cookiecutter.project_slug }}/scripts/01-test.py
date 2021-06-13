#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.full_name }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
from __future__ import absolute_import, division, print_function, with_statement

from src import *

def main():
    pass


if __name__ == '__main__':
    logger = setup_logger()     # this sets up the logger according to the definition in ./src/__init__.py
    main()                      # now, the logger statements defined in main() use the new logger
    submodule.sub_fun()         # the same for any submodule logger statements that get piped through
