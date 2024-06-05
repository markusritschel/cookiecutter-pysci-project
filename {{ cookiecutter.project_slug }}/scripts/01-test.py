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
from src.submodule import generate_int_list

# This is only necessary if this file gets imported by another one so that logs get piped
logger = logging.getLogger(__name__)
# Alternatively, set `logger = setup_logger()` as shown below.


def main():
    logger.info("Calling main function, doing nothing")


if __name__ == '__main__':
    logger = setup_logger()
    main()
    logger.info("Calling function from submodule")
    mylist = generate_int_list(6)
    print(mylist)
