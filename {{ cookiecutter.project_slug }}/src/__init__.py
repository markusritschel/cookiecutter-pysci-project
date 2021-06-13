import inspect
import logging
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

__version__ = '{{ cookiecutter.project_version }}'

# Make some of the basic directories globally available in your environment
base_dir = Path(__file__).resolve().parents[1]
data_dir = base_dir / 'data'
log_dir  = base_dir / 'logs'
plot_dir = base_dir / 'reports/figures'

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)



def setup_logger(level=None, logfile=True, name="root"):
    """Define a logger setup with
    - 1x fileHandler: writing log files to log_dir (logfile can be boolean or a file path)
    - 1x streamHandler: streaming logs to terminal

    Parameters
    ----------
    level : logLevel / str
        The log level (according to the logging convention). Can be either a string or a 
        loggin.loglevel instance
    logfile : bool / str
        If True, the log file will be placed in log_dir and named after the calling script (default)
        If logfile is a string, it will be interpreted as a file path (the parent directory must exist)
    
    Return
    ------
    logger
        The logger instance
    """
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
            logfile = log_dir / f'{caller_filename}_{os.getpid()}.log'
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
