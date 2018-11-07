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


@user.command()
@click.argument("email_address", required=False)
def email(email_address):
    """Display / set / update the user email."""
    if not email_address:
        click.secho(dtool_config.utils.get_user_email(CONFIG_PATH))
    else:
        click.secho(dtool_config.utils.set_user_email(
            CONFIG_PATH,
            email_address
        ))


@config.group()
def ecs():
    """Configure ECS S3 object storage."""


@ecs.command()
@click.argument("url", required=False)
def endpoint(url):
    """Display / set / update the ECS endpoint URL."""
    if not url:
        click.secho(dtool_config.utils.get_ecs_endpoint(CONFIG_PATH))
    else:
        click.secho(dtool_config.utils.set_ecs_endpoint(CONFIG_PATH, url))


@ecs.command()
@click.argument("ecs_access_key_id", required=False)
def access_key_id(ecs_access_key_id):
    """Display / set / update the ECS access key id."""
    if not ecs_access_key_id:
        click.secho(dtool_config.utils.get_ecs_access_key_id(CONFIG_PATH))
    else:
        click.secho(dtool_config.utils.set_ecs_access_key_id(
            CONFIG_PATH,
            ecs_access_key_id
        ))


@ecs.command()
@click.argument("ecs_secret_access_key", required=False)
def secret_access_key(ecs_secret_access_key):
    """Display / set / update the ECS secret access key."""
    if not ecs_secret_access_key:
        click.secho(dtool_config.utils.get_ecs_secret_access_key(CONFIG_PATH))
    else:
        click.secho(dtool_config.utils.set_ecs_secret_access_key(
            CONFIG_PATH,
            ecs_secret_access_key
        ))
