import os
import logging


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    WHITE = "\033[97m"   
    WHITE_BOLD = "\033[1;97m"   
    GREY = "\033[90m"
    LIGHT_GREY = "\033[37m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED_BOLD = "\033[1;31m"

    # Reset color
    RESET = "\033[0m"

    # Spaziatura
    # "INFO:     "
    # "DEBUG:    "
    # "WARNING:  "
    # "ERROR:    "
    # "CRITICAL: "

    message  = '%(message)s'
    filename = '{%(pathname)s:%(lineno)d}'
    time     = '[%(asctime)s]'
    process  = 'p%(process)s'
    
    level     = '%(levelname)s:'

    space_info     = '     '
    space_debug    = '    '
    space_warning  = '  '
    space_error    = '    '
    space_critical = ' '

    FORMATS = {
        logging.INFO:     GREEN    + level + RESET + space_info     + WHITE + message + RESET + ' ' + CYAN + filename + RESET + ' ' + GREY + time + RESET + ' ' + MAGENTA + process + RESET,
        logging.DEBUG:    BLUE     + level + RESET + space_debug    + WHITE + message + RESET + ' ' + CYAN + filename + RESET + ' ' + GREY + time + RESET + ' ' + MAGENTA + process + RESET,
        logging.WARNING:  YELLOW   + level + RESET + space_warning  + WHITE + message + RESET + ' ' + CYAN + filename + RESET + ' ' + GREY + time + RESET + ' ' + MAGENTA + process + RESET,
        logging.ERROR:    RED      + level + RESET + space_error    + WHITE + message + RESET + ' ' + CYAN + filename + RESET + ' ' + GREY + time + RESET + ' ' + MAGENTA + process + RESET,
        logging.CRITICAL: RED_BOLD + level + RESET + space_critical + WHITE + message + RESET + ' ' + CYAN + filename + RESET + ' ' + GREY + time + RESET + ' ' + MAGENTA + process + RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%m-%d %H:%M:%S")
        return formatter.format(record)


def setup_logger(name):
    logger = logging.getLogger(name)

    # get environment
    node_env = os.getenv("NODE_ENV", None)
    if node_env is not None and type(node_env) is str and len(node_env) > 0:
        development = node_env
    else:
        development = None

    # define logging level
    if development is not None:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if len(logger.handlers) > 0:
        return logger

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # Adjust as needed: DEBUG, INFO

    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    return logger

# Example usage
# logger = setup_logger(__name__)
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
