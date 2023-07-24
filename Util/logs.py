import inspect
import logging
from definitions import ROOT_DIR
import datetime
import os


LOGS_FOLDER_PATH = ROOT_DIR + "\\ResultFiles\\Logs\\"


def getLogger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler = logging.FileHandler(LOGS_FOLDER_PATH + 'logfile.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    return logger


# class Log:
#     LOGS_FOLDER_PATH = ROOT_DIR + "\\ResultFiles\\Logs\\"
#     LOG_FILE_NAME = "logfile.log"
#     LOG_FILE_PATH = os.path.join(LOGS_FOLDER_PATH, LOG_FILE_NAME)
#
#     @staticmethod
#     def create_logfile_if_not_present():
#         # Create the log folder if it doesn't exist
#         os.makedirs(Log.LOGS_FOLDER_PATH, exist_ok=True)
#
#         # Create the log file if it doesn't exist
#         if not os.path.exists(Log.LOG_FILE_PATH):
#             open(Log.LOG_FILE_PATH, 'w').close()
#
#     @staticmethod
#     def getLogger():
#         Log.create_logfile_if_not_present()
#
#         logger_name = inspect.stack()[1][3]
#         logger = logging.getLogger(logger_name)
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
#         file_handler = logging.FileHandler(Log.LOG_FILE_PATH)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)
#         logger.setLevel(logging.DEBUG)
#         return logger
