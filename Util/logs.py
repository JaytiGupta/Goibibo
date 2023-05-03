import inspect
import logging
from definitions import ROOT_DIR
import datetime


def getLogger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    # current_datetime = datetime.datetime.now()
    # log_file_name = current_datetime.strftime("Log" + "%Y_%m_%d-%H_%M_%S%f" + ".log")
    file_handler = logging.FileHandler(ROOT_DIR + f"\\ResultFiles\\Logs\\" + 'logfile.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    return logger

