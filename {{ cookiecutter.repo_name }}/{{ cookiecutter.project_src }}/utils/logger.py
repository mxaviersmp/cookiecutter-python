import logging
import os

try:
    from rich.logging import RichHandler
    RICH = True
except ImportError:
    RICH = False

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOG_FILE = os.getenv('LOG_FILE', None)

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

if RICH:
    shell_handler = RichHandler()
    fmt_shell = '%(message)s'
else:
    shell_handler = logging.StreamHandler()
    fmt_shell = '%(levelname)s %(asctime)s %(message)s'

shell_handler.setLevel(logging.DEBUG)
shell_formatter = logging.Formatter(fmt_shell)
shell_handler.setFormatter(shell_formatter)
logger.addHandler(shell_handler)

if LOG_FILE:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)
    fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
    file_formatter = logging.Formatter(fmt_file)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
