"""Helper functions for getting and setting config values."""

import os
import json

USERNAME_KEY = "DTOOL_USER_FULL_NAME"


def _get_config_content(config_fpath):

    # Default (empty) content will be used if config file does not exist.
    config_content = {}

    # If the config file exists we use that content.
    if os.path.isfile(config_fpath):
        with open(config_fpath) as fh:
            config_content = json.load(fh)

    return config_content


def _get(config_fpath, key):

    config_content = _get_config_content(config_fpath)

    if key not in config_content:
        return ""

    return config_content[key]


def _set(config_fpath, key, value):

    config_content = _get_config_content(config_fpath)

    # Add/update the key/value pair.
    config_content[key] = value

    with open(config_fpath, "w") as fh:
        json.dump(config_content, fh)

    return _get(config_fpath, key)


def get_username(config_fpath):
    """Return the user name.

    :param config_fpath: path to the dtool config file
    :returns: the user name or an empty string
    """
    return _get(config_fpath, USERNAME_KEY)


def set_username(config_fpath, username):
    """Write the user name to the dtool config file.

    :param config_fpath: path to the dtool config file
    :param username: user name
    """
    return _set(config_fpath, USERNAME_KEY, username)
