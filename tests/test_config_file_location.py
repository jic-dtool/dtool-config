"""Test the location of the dtool config file."""

def test_dtool_config_file_location():
    import dtoolcore.utils
    import dtool_config.cli

    assert dtool_config.cli.CONFIG_PATH == dtoolcore.utils.DEFAULT_CONFIG_PATH
