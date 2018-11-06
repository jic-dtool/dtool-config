"""dtool_config.cli module."""

import click

import dtoolcore.utils

import dtool_config.utils


CONFIG_PATH = dtoolcore.utils.DEFAULT_CONFIG_PATH


@click.group()
def config():
    """Configure dtool settings."""


@config.group()
def user():
    """Configure user settings."""


@user.command()
@click.argument("username", required=False)
def name(username):
    """Display / set / update the user name."""
    if not username:
        click.secho(dtool_config.utils.get_username(CONFIG_PATH))
    else:
        click.secho(dtool_config.utils.set_username(CONFIG_PATH, username))
