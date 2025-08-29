"""
Time and astronomical utilities for Python
==========================================

timescale contains Python tools for time and astronomical calculations.

Documentation is available at https://timescale.readthedocs.io
"""
import timescale.eop
import timescale.time
import timescale.utilities
import timescale.version

# shortcut wrapper functions for timescale.time.Timescale methods
# delta time
def from_deltatime(*args, **kwargs):
    """Wrapper for ``timescale.time.Timescale().from_deltatime``
    """
    return timescale.time.Timescale.from_deltatime(*args, **kwargs)
# Julian dates
def from_julian(ut1, **kwargs):
    return timescale.time.Timescale(ut1 - 2400000.5)
# Besselian years
def from_besselian(B, **kwargs):
    """Wrapper for creating a ``Timescale`` object from Besselian years
    """
    # convert Besselian year to MJD
    MJD = 15019.81352 + (B - 1900.0) * 365.242198781
    return timescale.time.Timescale(MJD)
# calendar dates
def from_calendar(*args, **kwargs):
    """Wrapper for ``timescale.time.Timescale().from_calendar``
    """
    return timescale.time.Timescale.from_calendar(*args, **kwargs)
# datetime arrays
def from_datetime(*args, **kwargs):
    """Wrapper for ``timescale.time.Timescale().from_datetime``
    """
    return timescale.time.Timescale.from_datetime(*args, **kwargs)
# range of dates
def from_range(start, end, *args, **kwargs):
    """Wrapper for creating a ``Timescale`` object from a range of dates
    """
    d = timescale.time.date_range(start, end, *args, **kwargs)
    return timescale.time.Timescale.from_datetime(d)
# list of timescale objects
def from_list(*args, **kwargs):
    """Wrapper for ``timescale.time.Timescale().from_list``
    """
    return timescale.time.Timescale.from_list(*args, **kwargs)

# get version information
__version__ = timescale.version.version
