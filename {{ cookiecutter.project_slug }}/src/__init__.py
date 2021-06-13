from pathlib import Path
from dotenv import find_dotenv, load_dotenv

__version__ = '{{ cookiecutter.project_version }}'

# Make some of the basic directories globally available in your environment
base_dir = Path(__file__).resolve().parents[1]
data_dir = base_dir / 'data'
log_dir  = base_dir / 'logs'
plot_dir = base_dir / 'reports/figures'
jupyter_startup_script = base_dir / 'notebooks/jupyter_startup.ipy'

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)



def setup_logger(level=None, logfile=True):
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

    # set up new logger and set level
    logger = logging.getLogger()
    logger.setLevel(level)

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
        fh = logging.FileHandler(logfile)
        fh.setFormatter(formatter)
        fh.setLevel(level)
        logger.addHandler(fh)
        logger.logfile = logfile.as_posix()
    else:
        logger.logfile = None

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

#     logger.info("="*(17+len(caller_file)))
#     logger.info("Calling routine: %s", caller_file)
#     if logfile:
#         logger.info("Log file: %s", logfile)
#     logger.info("-"*(17+len(caller_file))+"\n")

    return logger
