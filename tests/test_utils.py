"""Test the helper utility functions."""

import os

from . import tmp_dir_fixture  # NOQA


def test_missing_parent_config_dir(tmp_dir_fixture):  # NOQA
    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, ".config", "dtool.json")
    username = "Postman Pat"
    dtool_config.utils.set_username(config_fpath, username)

    assert dtool_config.utils.get_username(config_fpath) == username


def test_permissions_on_config_file(tmp_dir_fixture):  # NOQA
    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")
    username = "Postman Pat"
    dtool_config.utils.set_username(config_fpath, username)

    assert os.stat(config_fpath).st_mode == 33216


def test_set_get_name(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_username(config_fpath) == ""

    username = "Postman Pat"
    dtool_config.utils.set_username(config_fpath, username)
    assert dtool_config.utils.get_username(config_fpath) == username


def test_set_get_email(tmp_dir_fixture):  # NOQA
    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_user_email(config_fpath) == ""

    email = "pat@example.com"
    dtool_config.utils.set_user_email(config_fpath, email)
    assert dtool_config.utils.get_user_email(config_fpath) == email

    email = "postman.pat@example.com"
    dtool_config.utils.set_user_email(config_fpath, email)
    assert dtool_config.utils.get_user_email(config_fpath) == email


def test_set_get_ecs_endpoint(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_ecs_endpoint(config_fpath) == ""

    ecs_endpoint = "http://blueberry.famous.uni.ac.uk"
    dtool_config.utils.set_ecs_endpoint(config_fpath, ecs_endpoint)
    assert dtool_config.utils.get_ecs_endpoint(config_fpath) == ecs_endpoint


def test_set_get_ecs_access_key_id(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_ecs_access_key_id(config_fpath) == ""

    acc_key_id = "patp"
    dtool_config.utils.set_ecs_access_key_id(config_fpath, acc_key_id)
    assert dtool_config.utils.get_ecs_access_key_id(config_fpath) == acc_key_id


def test_set_get_ecs_secret_access_key(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_ecs_secret_access_key(config_fpath) == ""

    key = "secret"
    dtool_config.utils.set_ecs_secret_access_key(config_fpath, key)
    assert dtool_config.utils.get_ecs_secret_access_key(config_fpath) == key


def test_set_ls_cache(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_cache(config_fpath, "ecs") == ""

    ecs_cache_dir = os.path.join(tmp_dir_fixture, "ecs")
    dtool_config.utils.set_cache(config_fpath, "ecs", ecs_cache_dir)
    assert dtool_config.utils.get_cache(config_fpath, "ecs") == ecs_cache_dir
