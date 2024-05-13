# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: Markus Ritschel
# eMail:  git@markusritschel.de
# Date:   2024-05-07
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
import inspect
import logging
import os
from pathlib import Path

log = logging.getLogger(__name__)

__all__ = ["setup_logger", "save"]


def setup_logger(level=None, logfile=True, name="root"):
    """Define a logger setup with
    - 1x fileHandler: writing log files to LOG_DIR (logfile can be boolean or a file path)
    - 1x streamHandler: streaming logs to terminal

    Parameters
    ----------
    level : logLevel / str
        The log level (according to the logging convention). Can be either a string or a 
        loggin.loglevel instance
    logfile : bool / str
        If True, the log file will be placed in LOG_DIR and named after the calling script (default)
        If logfile is a string, it will be interpreted as a file path (the parent directory must exist)
    
    Return
    ------
    logger
        The logger instance
    """
    from src import LOG_DIR

    caller_file = inspect.stack()[-1].filename
    caller_filename = Path(caller_file).stem

    if not level:
        level = os.getenv('LOGLEVEL', 'INFO').upper()
    print("LOGLEVEL:", level)

    # set up new logger and set level to DEBUG to ensure that all messages are written to the log file
    logger = logging.getLogger()
    logger.setLevel('DEBUG')

    formatter = logging.Formatter('%(asctime)s: '
                                  '[%(levelname)s] '
                                  # '(%(name)s): '
                                  '(%(name)s:#%(lineno)d): '
                                  '%(message)s'
                                  , datefmt='%Y-%m-%d %H:%M:%S')
    
    if logfile:
        if isinstance(logfile, bool):
            logfile = LOG_DIR / f'{caller_filename}_{os.getpid()}.log'
        elif isinstance(logfile, str):
            logdir = Path(logfile).parents[0]
            if not logdir.exists():
                raise IOError(f'Log directory {logdir} does not exist.')
        logger.logfile = logfile.as_posix()
        print(f"Log file: {logger.logfile}")
        
        filehandler = logging.FileHandler(logfile)
        filehandler.setFormatter(formatter)
        filehandler.setLevel('DEBUG')
        logger.addHandler(filehandler)
    else:
        logger.logfile = None

    streamhandler = logging.StreamHandler()
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    logger.info("="*(17+len(caller_file)))
    logger.info("Calling routine: %s", caller_file)
    logger.info("-"*(17+len(caller_file))+"\n")

    return logger
