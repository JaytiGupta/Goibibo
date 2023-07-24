from Util.logs import getLogger
from definitions import global_dict
from pytest import fixture


def test_mytest(pc, test_fixture):
    log = getLogger()
    print(test_fixture)
    log.info(global_dict["take_screenshots"])
    log.info(global_dict["env"])


@fixture()
def test_fixture():
    return "test_fixture123"