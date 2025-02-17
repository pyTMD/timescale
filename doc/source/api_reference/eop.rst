===
eop
===

Utilities for maintaining Earth Orientation Parameter (EOP) files

- Syncs mean pole files with IERS servers
- Can calculate update mean pole files using data from IERS servers
- Syncs finals orientation files with IERS servers

`Source code`__

.. __: https://github.com/pyTMD/timescale/blob/main/timescale/eop.py


General Methods
===============

.. autofunction:: timescale.eop.update_mean_pole

.. autofunction:: timescale.eop.calculate_mean_pole

.. autofunction:: timescale.eop.pull_pole_coordinates

.. autofunction:: timescale.eop.update_finals_file

.. autofunction:: timescale.eop.iers_mean_pole

.. autofunction:: timescale.eop.iers_daily_EOP

.. autofunction:: timescale.eop.iers_polar_motion
