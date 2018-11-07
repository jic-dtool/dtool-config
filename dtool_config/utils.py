"""Helper functions for getting and setting config values."""

import os
import json

from dtoolcore.utils import mkdir_parents

USERNAME_KEY = "DTOOL_USER_FULL_NAME"
USER_EMAIL_KEY = "DTOOL_USER_EMAIL"


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

    # Create parent directories if they are missing.
    mkdir_parents(os.path.dirname(config_fpath))

    with open(config_fpath, "w") as fh:
        json.dump(config_content, fh, sort_keys=True, indent=2)

    os.chmod(config_fpath, 33216)

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


def get_user_email(config_fpath):
    """Return the user email.

    :param config_fpath: path to the dtool config file
    :returns: the user email or an empty string
    """
    return _get(config_fpath, USER_EMAIL_KEY)


def set_user_email(config_fpath, email):
    """Write the user email to the dtool config file.

    :param config_fpath: path to the dtool config file
    :param email: user email
    """
    return _set(config_fpath, USER_EMAIL_KEY, email)
