from Util.logs import getLogger
from pytest import mark


@mark.skip
def test_new(env, take_screenshots, guidewire):
    print(f"\nEnvironment: {env}")
    print(f"Taking Screenshots: {take_screenshots} ")
