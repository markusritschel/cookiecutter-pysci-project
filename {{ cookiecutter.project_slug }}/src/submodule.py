"""This submodule exists only for demonstration purposes.
To show the concept of the logger setup and running a pytest.
"""
import logging

logger = logging.getLogger(__name__)

def sub_fun(x: int) -> list[int]:
    """This is a doctest in a docstring. You can link to other functions, e.g. :func:`src.setup_logger`.

    Example
    -------
    >>> sub_fun(3)
    [1, 2, 3]
    """
    logger.info("From sub-module")
    return list(range(1,x+1))
