"""Test the dtool_config package."""


def test_version_is_string():
    import dtool_config
    assert isinstance(dtool_config.__version__, str)
