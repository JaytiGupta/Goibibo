# test_sample.py

import time
from Util.logs import getLogger


def test_case_1():
    time.sleep(2)
    log = getLogger()

    log.info("Test case 1 Running...")
    time.sleep(2)
    log.info("Test case 1: Running...")
    assert 1 + 1 == 2


def test_case_2():
    time.sleep(2)
    log = getLogger()

    log.info("Test case 2 Running...")
    time.sleep(2)
    log.info("Test case 2: Running...")
    assert 2 * 3 == 6


# @mark.skip
# def test_new(env, take_screenshots, guidewire):
#     print(f"\nEnvironment: {env}")
#     print(f"Taking Screenshots: {take_screenshots} ")
