#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.project_author }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
"""The functions below only serve for demonstrating the logger setup. Feel free to delete them 
as well as this docstring once the concept is understood :-)"""
from __future__ import absolute_import, division, print_function, with_statement
import logging

from src import *
from src import submodule

# This is only necessary if this file gets imported by another one so that logs get piped
logger = logging.getLogger(__name__)


def main():
    logger.info("Test")


if __name__ == '__main__':
    logger = setup_logger()     # this sets up the logger according to the definition in ./src/__init__.py
    main()                      # now, the logger statements defined in main() use the new logger
    submodule.sub_fun()         # the same for any submodule logger statements that get piped through
