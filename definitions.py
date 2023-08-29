import os
from Util.config import AppConfig

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
AVAILABLE_ENVIRONMENT = ("test", "dev")
CONFIG = AppConfig(AVAILABLE_ENVIRONMENT)


# TODO exception handling
# TODO reporting
# TODO logs - separate file creation for each run
