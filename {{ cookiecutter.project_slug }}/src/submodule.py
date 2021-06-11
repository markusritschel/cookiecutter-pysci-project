"""This submodule exists only for demonstration purposes.
To show the concept of the logger setup and running a pytest.
"""
import logging

logger = logging.getLogger(__name__)

def sub_fun():
    """ a doctest in a docstring
    >>> sub_fun()
    [1, 2, 3]
    """
    logger.info("From sub-module")
    return [1,2,3]
