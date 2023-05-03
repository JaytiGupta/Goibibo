import inspect
import logging
from definitions import ROOT_DIR
print(ROOT_DIR)

def getLogger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler = logging.FileHandler(ROOT_DIR + "\\Test Files\\Logs\\" + 'logfile.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    return logger

