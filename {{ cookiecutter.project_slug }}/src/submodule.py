"""This submodule exists only for demonstration purposes.
"""
import logging

logger = logging.getLogger(__name__)

def sub_fun():
    logger.info("From sub-module")
    return