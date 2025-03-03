===============
Getting Started
===============

This documentation is intended to explain how to compute time conversions and offsets using ``timescale``.

Time
####

The `time module <https://github.com/pyTMD/timescale/blob/main/timescale/time.py>`_ within ``timescale`` can convert different time formats to the necessary time format of a given program.
The `time module <https://github.com/pyTMD/timescale/blob/main/timescale/time.py>`_ can also parse date strings describing the units and epoch of relative times, or the calendar date of measurement for geotiff formats.
``timescale`` keeps updated `tables of leap seconds <https://github.com/pyTMD/timescale/blob/main/timescale/data/leap-seconds.list>`_ for converting from GPS, LORAN and TAI times.

- TAI time: International Atomic Time which is computed as the weighted average of several hundred atomic clocks.
- UTC time: Coordinated Universal Time which is `periodically adjusted <https://www.nist.gov/pml/time-and-frequency-division/leap-seconds-faqs>`_ to account for the difference between the definition of the second and the rotation of Earth.
- GPS time: Atomic timing system for the Global Positioning System constellation of satellites monitored by the United States Naval Observatory (USNO). GPS time and UTC time were equal on January 6, 1980. TAI time is ahead of GPS time by 19 seconds.
- LORAN time: Atomic timing system for the Loran-C chain transmitter sites used in terrestrial radionavigation. LORAN time and UTC time were equal on January 1, 1958. TAI time is ahead of LORAN time by 10 seconds.

``timescale`` also keeps updated `tables of delta times <https://github.com/pyTMD/timescale/blob/main/timescale/data/merged_deltat.data>`_ for converting between dynamic (TT) and universal (UT1) times.
Delta times (TT - UT1) are the differences between Dynamic Time (TT) and Universal Time (UT1) :cite:p:`Meeus:1991vh`.
Universal Time (UT1) is based on the rotation of the Earth,
which varies irregularly, and so UT1 is adjusted periodically.
Dynamic Time (TT) is a uniform, monotonically increasing time standard based on atomic clocks that is
used for the accurate calculation of celestial mechanics, orbits and ephemerides.
Delta times can be added to Universal Time (UT1) values to convert to Dynamic Time (TT) values.

Programs
########

``Timescale`` objects can be used to convert between date and time formats.
There are a few different ways to create a ``Timescale`` object:

1. range of dates

.. code-block:: python

    import timescale.time
    ts = timescale.from_range('2018-01-01','2018-12-31', 1)

2. delta times

.. code-block:: python

    import numpy as np
    import timescale.time
    delta_time = np.arange(365)*timescale.time._to_sec['day']
    ts = timescale.from_deltatime(delta_time, epoch=(2018,1,1,0,0,0))

3. ``datetime`` objects

.. code-block:: python

    import datetime
    import timescale.time
    date = datetime.datetime(2018,1,1,0,0,0)
    ts = timescale.from_datetime(date)

4. calendar dates

.. code-block:: python

    import numpy as np
    import timescale.time
    year = 2018
    month = 1
    day = 1 + np.arange(31)
    ts = timescale.from_calendar(year, month, day)

5. Julian dates

.. code-block:: python

    import numpy as np
    import timescale.time
    JD = np.arange(2458119.5, 2458150.5, 1)
    ts = timescale.from_julian(JD)

``Timescale`` objects can be used to convert epochs, convert to different time standards, convert to ``datetime`` arrays, and other time conversions.
See the `API Reference <../api_reference/time.html#timescale.time.Timescale>`_ for more information.
