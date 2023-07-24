import json
from dataclasses import dataclass
from definitions import ROOT_DIR


CONFIG_FOLDER_PATH = ROOT_DIR + "\\Data\\config\\"


def get_configuration(environment):
    config_file = CONFIG_FOLDER_PATH + f'config_{environment}.json'
    with open(config_file, 'r') as file:
        config_data = json.load(file)

    return config_data


@dataclass
class ConfigObjectClass:
    base_url: str
    username: str
    password: str
    timeout: int


def config_test(environment):
    config = get_configuration(environment)
    config_object = ConfigObjectClass(**config)
    return config_object


# a = config_test("test")
# print(a.username)

if __name__ == "__main__":
    env = "test"

    b = config_test(env)
    print(b.base_url)
    print(b.username)
    print(b.password)
    print(b.timeout)


