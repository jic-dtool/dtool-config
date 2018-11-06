"""Test the helper utility functions."""

import os

from . import tmp_dir_fixture  # NOQA


def test_set_get_name(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_username(config_fpath) == ""

    username = "Postman Pat"
    dtool_config.utils.set_username(config_fpath, username)
    assert dtool_config.utils.get_username(config_fpath) == username

