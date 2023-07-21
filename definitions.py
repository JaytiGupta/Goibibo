import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# TODO: Put screenshot and env variables in some other dict like config
global_dict = {
    "env": "test",
    "take_screenshots": False,
}


def set_value(key, value):
    global_dict[key] = value


# TODO exception handling
# TODO reporting
# TODO logs - separate file creation for each run
# Add 8-10 test cases with lists/collections etc...   ----- 1 with each feature
# TODO parallel/linear execution ------- 6
# pass URL as parameter  ------ 1
# github (try this first) /gitlab ------ 4