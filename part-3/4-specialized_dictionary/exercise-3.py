"""
Write a function that has a single argument (env name) and returns the "combined" dictionary
that merge 2 dictionaries together with the environment specific settings overriding any common settings already defined
"""
import json
from contextlib import ExitStack
from collections import ChainMap


# Declare setting files' name
SETTINGS_FILES = ['common.json', 'dev.json', 'prod.json']

# Read file
with ExitStack() as stack:
    SETTINGS = {
        f_name.split('.')[0]: json.load(stack.enter_context(open(f_name)))
        for f_name in SETTINGS_FILES
    }

# Choose which setting is the base
BASE_SETTINGS = 'common'


def chain_recursive_fred(overrided, base):
    chain = ChainMap(overrided, base)
    for k, v in overrided.items():
        if isinstance(v, dict) and k in base:
            chain[k] = chain_recursive_fred(v, base[k])
    return chain


def settings_for_env(env):
    result = chain_recursive_fred(SETTINGS[env], SETTINGS[BASE_SETTINGS])
    return result


dev = settings_for_env('dev')
print(dev)
