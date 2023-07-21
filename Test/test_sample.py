from Util.logs import getLogger
from definitions import global_dict


def test_mytest(browser, login_data):
    log = getLogger()
    log.info(global_dict["take_screenshots"])
    log.info(global_dict["env"])
