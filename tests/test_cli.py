"""Test the dtool config command line interface."""

import json

import pytest
from click.testing import CliRunner


@pytest.fixture
def config_path(tmp_path, monkeypatch):
    """Point the CLI at a temporary config file, never the user's own."""
    import dtool_config.cli

    path = tmp_path / "dtool.json"
    monkeypatch.setattr(dtool_config.cli, "CONFIG_PATH", str(path))
    return path


def run(*args):
    """Invoke ``dtool config`` with ``args``; return its stripped output."""
    from dtool_config.cli import config

    result = CliRunner().invoke(config, [str(a) for a in args])
    assert result.exit_code == 0, result.output
    return result.output.strip()


def stored(config_path):
    return json.loads(config_path.read_text())


def test_user_name(config_path):
    assert run("user", "name") == ""
    assert run("user", "name", "Postman", "Pat") == "Postman Pat"
    assert run("user", "name") == "Postman Pat"
    assert stored(config_path)["DTOOL_USER_FULL_NAME"] == "Postman Pat"


def test_user_email(config_path):
    assert run("user", "email") == ""
    assert run("user", "email", "pat@example.com") == "pat@example.com"
    assert run("user", "email") == "pat@example.com"


def test_readme_template(config_path, tmp_path):
    template = tmp_path / "README.yml"
    template.write_text("description: a template\n")

    assert run("readme-template") == ""
    assert run("readme-template", template) == str(template)
    assert run("readme-template") == str(template)


def test_readme_template_must_exist(config_path, tmp_path):
    from dtool_config.cli import config

    result = CliRunner().invoke(
        config, ["readme-template", str(tmp_path / "missing.yml")])
    assert result.exit_code != 0
    assert not config_path.exists()


def test_cache(config_path, tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()

    assert run("cache") == ""
    assert run("cache", cache) == str(cache)
    assert run("cache") == str(cache)


def test_ecs(config_path):
    bucket = "my-bucket"
    url = "https://ecs.example.com"

    assert run("ecs", "endpoint", bucket) == ""
    assert run("ecs", "endpoint", bucket, url) == url
    assert run("ecs", "endpoint", bucket) == url

    assert run("ecs", "access-key-id", bucket) == ""
    assert run("ecs", "access-key-id", bucket, "key-id") == "key-id"
    assert run("ecs", "access-key-id", bucket) == "key-id"

    assert run("ecs", "secret-access-key", bucket) == ""
    assert run("ecs", "secret-access-key", bucket, "secret") == "secret"
    assert run("ecs", "secret-access-key", bucket) == "secret"

    assert run("ecs", "ls") == "ecs://my-bucket"


def test_azure(config_path):
    assert run("azure", "ls") == ""
    assert run("azure", "get", "container") == ""
    assert run("azure", "set", "container", "secret") == "secret"
    assert run("azure", "get", "container") == "secret"
    run("azure", "set", "other", "secret2")
    assert run("azure", "ls").split() == ["azure://container", "azure://other"]
