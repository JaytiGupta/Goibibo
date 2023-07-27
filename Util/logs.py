from definitions import ROOT_DIR
import logging
import inspect
import os


LOGS_FOLDER_PATH = ROOT_DIR + "\\ResultFiles\\Logs\\"
LOG_FILE_PATH = os.path.join(LOGS_FOLDER_PATH, 'logfile.log')


def getLogger():
    # Create the logs folder if it doesn't exist
    os.makedirs(LOGS_FOLDER_PATH, exist_ok=True)

    # Create the log file if not present, and set up the file handler
    with open(LOG_FILE_PATH, 'a'):
        pass  # Just create the file and close it

    # Configure the log format
    log_format = "%(asctime)s [%(levelname)s] %(name)s :%(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    logger_name = inspect.stack()[1][3]

    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    return logger
