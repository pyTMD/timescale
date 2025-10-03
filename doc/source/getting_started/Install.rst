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

Development Install
###################

To use the development repository, please fork ``timescale`` into your own account and then clone onto your system:

.. code-block:: bash

    git clone https://github.com/pyTMD/timescale.git

``timescale`` can then be installed within the package directory using ``pip``:

.. code-block:: bash

    python3 -m pip install --user .

The development version of ``timescale`` can also be installed directly from GitHub using ``pip``:

.. code-block:: bash

    python3 -m pip install --user git+https://github.com/pyTMD/timescale.git

Package Management with ``pixi``
################################

Alternatively ``pixi`` can be used to create a `streamlined environment <https://pixi.sh/>`_ after cloning the repository:

.. code-block:: bash

    pixi install

``pixi`` maintains isolated environments for each project, allowing for different versions of
``timescale`` and its dependencies to be used without conflict. The ``pixi.lock`` file within the
repository defines the required packages and versions for the environment.

``pixi`` can also create shells for running programs within the environment:

.. code-block:: bash

    pixi shell

To see the available tasks within the ``timescale`` workspace:

.. code-block:: bash

    pixi task list

.. note::

    ``pixi`` is under active development and may change in future releases
