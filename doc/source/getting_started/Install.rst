======================
Setup and Installation
======================

``timescale`` is available for download from the `GitHub repository <https://github.com/pyTMD/timescale>`_,
the `Python Package Index (pypi) <https://pypi.org/project/timescale/>`_,
and from `conda-forge <https://anaconda.org/conda-forge/timescale>`_.


The simplest installation for most users will likely be using ``conda`` or ``mamba``:

.. code-block:: bash

    conda install -c conda-forge timescale

``conda`` installed versions of ``timescale`` can be upgraded to the latest stable release:

.. code-block:: bash

    conda update timescale

To use the development repository, please fork ``timescale`` into your own account and then clone onto your system:

.. code-block:: bash

    git clone https://github.com/pyTMD/timescale.git

``timescale`` can then be installed within the package directory using ``pip``:

.. code-block:: bash

    python3 -m pip install --user .

The development version of ``timescale`` can also be installed directly from GitHub using ``pip``:

.. code-block:: bash

    python3 -m pip install --user git+https://github.com/pyTMD/timescale.git
