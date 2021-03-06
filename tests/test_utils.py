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


def test_set_get_readme_template_fpath(tmp_dir_fixture):  # NOQA
    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_readme_template_fpath(config_fpath) == ""

    template_fpath = os.path.join(tmp_dir_fixture, "readme.yml")
    with open(template_fpath, "w") as fh:
        fh.write("---/ndescription: something\n")

    dtool_config.utils.set_readme_template_fpath(config_fpath, template_fpath)
    assert dtool_config.utils.get_readme_template_fpath(config_fpath) == template_fpath  # NOQA

    template_fpath_alt = os.path.join(tmp_dir_fixture, "readme_alt.yml")
    with open(template_fpath_alt, "w") as fh:
        fh.write("---/ndescription: something else\n")

    dtool_config.utils.set_readme_template_fpath(config_fpath, template_fpath_alt)  # NOQA
    assert dtool_config.utils.get_readme_template_fpath(config_fpath) == template_fpath_alt  # NOQA


def test_set_get_ecs_endpoint(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_ecs_endpoint(config_fpath, "demo") == ""

    ecs_endpoint = "http://blueberry.famous.uni.ac.uk"
    dtool_config.utils.set_ecs_endpoint(config_fpath, "demo", ecs_endpoint)
    assert dtool_config.utils.get_ecs_endpoint(config_fpath, "demo") == ecs_endpoint  # NOQA


def test_set_get_ecs_access_key_id(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_ecs_access_key_id(config_fpath, "demo") == ""

    acc_key_id = "patp"
    dtool_config.utils.set_ecs_access_key_id(config_fpath, "demo", acc_key_id)
    assert dtool_config.utils.get_ecs_access_key_id(config_fpath, "demo") == acc_key_id  # NOQA

    assert dtool_config.utils.list_ecs_base_uris(config_fpath) == ["ecs://demo"]  # NOQA


def test_set_get_ecs_secret_access_key(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_ecs_secret_access_key(config_fpath, "demo") == "" # NOQA

    key = "secret"
    dtool_config.utils.set_ecs_secret_access_key(config_fpath, "demo", key)
    assert dtool_config.utils.get_ecs_secret_access_key(config_fpath, "demo") == key  # NOQA


def test_set_get_cache(tmp_dir_fixture):  # NOQA

    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert dtool_config.utils.get_cache(config_fpath) == ""

    cache_dir = os.path.join(tmp_dir_fixture, "dtool_cache")
    dtool_config.utils.set_cache(config_fpath, cache_dir)
    assert dtool_config.utils.get_cache(config_fpath) == cache_dir


def test_set_get_azure_container(tmp_dir_fixture):  # NOQA
    import dtool_config.utils

    config_fpath = os.path.join(tmp_dir_fixture, "dtool.json")

    assert "" == dtool_config.utils.get_azure_secret_access_key(
        config_fpath,
        "demo"
    )

    token = "secret"
    dtool_config.utils.set_azure_secret_access_key(config_fpath, "demo", token)
    assert token == dtool_config.utils.get_azure_secret_access_key(
        config_fpath,
        "demo"
    )

    dtool_config.utils.set_azure_secret_access_key(config_fpath, "prod", "s2")

    containers = ["azure://demo", "azure://prod"]
    assert containers == dtool_config.utils.list_azure_base_uris(config_fpath)
