====
time
====

Utilities for calculating time operations

 - Can convert delta time from seconds since an epoch to time since a different epoch
 - Can calculate the time in days since epoch from calendar dates
 - Calculates the difference between dynamic time and universal time (`TT` - `UT1`)
 - Can count the number of leap seconds between a given GPS time and UTC
 - Syncs leap second files with NIST servers
 - Updates differences between universal time (`UT`) and dynamic time (`TT`)

Calling Sequence
----------------

Count the number of leap seconds between a GPS time and UTC

.. code-block:: python

    import timescale.time
    leap_seconds = timescale.time.count_leap_seconds(gps_seconds)

Convert a time from seconds since 1980-01-06T00:00:00 to Modified Julian Days (MJD)

.. code-block:: python

    import timescale.time
    MJD = timescale.time.convert_delta_time(delta_time, epoch1=(1980,1,6,0,0,0),
        epoch2=(1858,11,17,0,0,0), scale=1.0/86400.0)

Convert a calendar date into Modified Julian Days

.. code-block:: python

    import timescale.time
    MJD = timescale.time.convert_calendar_dates(YEAR,MONTH,DAY,hour=HOUR,
        minute=MINUTE,second=SECOND,epoch=(1858,11,17,0,0,0))

`Source code`__

.. __: https://github.com/pyTMD/timescale/blob/main/timescale/time.py


General Methods
===============

.. autofunction:: timescale.time.parse

.. autofunction:: timescale.time.parse_date_string

.. autofunction:: timescale.time.split_date_string

.. autofunction:: timescale.time.datetime_to_list

.. autofunction:: timescale.time.date_range

.. autofunction:: timescale.time.calendar_days

.. autofunction:: timescale.time.convert_datetime

.. autofunction:: timescale.time.convert_delta_time

.. autofunction:: timescale.time.convert_calendar_dates

.. autofunction:: timescale.time.convert_calendar_decimal

.. autofunction:: timescale.time.convert_julian

.. autoclass:: timescale.time.Timescale
   :members:

.. autoclass:: timescale.time.Calendar
   :members:

.. autofunction:: timescale.time.interpolate_delta_time

.. autofunction:: timescale.time.count_leap_seconds

.. autofunction:: timescale.time.get_leap_seconds

.. autofunction:: timescale.time.update_leap_seconds

.. autofunction:: timescale.time.merge_delta_time

.. autofunction:: timescale.time.append_delta_time

.. autofunction:: timescale.time.merge_bulletin_a_files

.. autofunction:: timescale.time.iers_ftp_delta_time

.. autofunction:: timescale.time.iers_delta_time

.. autofunction:: timescale.time.cddis_delta_time

.. autofunction:: timescale.time.read_iers_bulletin_a

.. autofunction:: timescale.time.update_bulletin_a

.. autofunction:: timescale.time.pull_deltat_file
