CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^


[0.4.1] - 2021-06-23
--------------------

Fixed
^^^^^

- Licence file now included in release thanks to Jan Janssen (https://github.com/jan-janssen)


[0.4.0] - 2019-07-12
--------------------

Added
^^^^^

- Added ``dtool config ecs ls`` command to list ECS base URIs that have been
  configured


Changed
^^^^^^^

- The ``dtool config azure ls`` command now returns base URIs rather than
  container names


[0.3.0] - 2019-05-14
--------------------

Added
^^^^^

- Support for configuring access to buckets in multiple namespaces


[0.2.0] - 2019-04-25
--------------------

Added
^^^^^

- ``dtool config readme-template`` CLI command for configuring the path to a
  custom readme template

Changed
^^^^^^^

- ``dtool config cache`` now works with one unified cache directory for all
  storage brokers

Fixed
^^^^^

- Fixed defect  when username was supplied as two separate strings to
  ``dtool config user name``


[0.1.1] - 2018-12-12
--------------------

Fixed
^^^^^

- Fix the ``dtool config azure set`` help text


[0.1.0] - 2018-11-08
--------------------

Initial release.
