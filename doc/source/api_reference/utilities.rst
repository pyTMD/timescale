=========
utilities
=========

Download and management utilities for syncing time and auxiliary files

 - Can list a directory on a ftp host
 - Can download a file from a ftp or http host
 - Can download a file from CDDIS via https when NASA Earthdata credentials are supplied
 - Checks ``MD5`` or ``sha1`` hashes between local and remote files

`Source code`__

.. __: https://github.com/pyTMD/timescale/blob/main/timescale/utilities.py


General Methods
===============

.. autofunction:: timescale.utilities.get_data_path

.. autoclass:: timescale.utilities.reify
   :members:

.. autofunction:: timescale.utilities.file_opener

.. autofunction:: timescale.utilities.get_hash

.. autofunction:: timescale.utilities.get_git_revision_hash

.. autofunction:: timescale.utilities.get_git_status

.. autofunction:: timescale.utilities.url_split

.. autofunction:: timescale.utilities.roman_to_int

.. autofunction:: timescale.utilities.get_unix_time

.. autofunction:: timescale.utilities.isoformat

.. autofunction:: timescale.utilities.even

.. autofunction:: timescale.utilities.ceil

.. autofunction:: timescale.utilities.copy

.. autofunction:: timescale.utilities.check_ftp_connection

.. autofunction:: timescale.utilities.ftp_list

.. autofunction:: timescale.utilities.from_ftp

.. autofunction:: timescale.utilities._create_default_ssl_context

.. autofunction:: timescale.utilities._create_ssl_context_no_verify

.. autofunction:: timescale.utilities._set_ssl_context_options

.. autofunction:: timescale.utilities.check_connection

.. autofunction:: timescale.utilities.http_list

.. autofunction:: timescale.utilities.from_http

.. autofunction:: timescale.utilities.attempt_login

.. autofunction:: timescale.utilities.build_opener

.. autofunction:: timescale.utilities.get_token

.. autofunction:: timescale.utilities.list_tokens

.. autofunction:: timescale.utilities.revoke_token

.. autofunction:: timescale.utilities.check_credentials

.. autofunction:: timescale.utilities.cddis_list

.. autofunction:: timescale.utilities.from_cddis

.. autofunction:: timescale.utilities.iers_list

.. autofunction:: timescale.utilities.from_jpl_ssd
