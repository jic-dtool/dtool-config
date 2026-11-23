"""dtool_config package."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("dtool-config")
except PackageNotFoundError:
    # Package is not installed.
    __version__ = "unknown"
