# timescale

[![License](https://img.shields.io/github/license/pyTMD/timescale)](https://github.com/pyTMD/timescale/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/timescale/badge/?version=latest)](https://timescale.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/timescale.svg)](https://pypi.python.org/pypi/timescale/)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/timescale)](https://anaconda.org/conda-forge/timescale)
[![commits-since](https://img.shields.io/github/commits-since/pyTMD/timescale/latest)](https://github.com/pyTMD/timescale/releases/latest)
[![zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.5555395.svg)](https://doi.org/10.5281/zenodo.5555395)

Python tools for time and astronomical calculations

For more information: see the documentation at [timescale.readthedocs.io](https://timescale.readthedocs.io/)

## Installation

From PyPI:

```bash
python3 -m pip install timescale
```

Using `conda` or `mamba` from conda-forge:

```bash
conda install -c conda-forge timescale
```

```bash
mamba install -c conda-forge timescale
```

Development version from GitHub:

```bash
python3 -m pip install git+https://github.com/pyTMD/timescale.git
```

### Running with Pixi

Alternatively, you can use [Pixi](https://pixi.sh/) for a streamlined workspace environment:

1. Install Pixi following the [installation instructions](https://pixi.sh/latest/#installation)
2. Clone the project repository:

```bash
git clone https://github.com/pyTMD/timescale.git
```

3. Move into the `timescale` directory

```bash
cd timescale
```

4. Install dependencies and start a shell to run programs:

```bash
pixi shell
```

## Dependencies

- [dateutil: powerful extensions to datetime](https://dateutil.readthedocs.io/en/stable/)
- [lxml: processing XML and HTML in Python](https://pypi.python.org/pypi/lxml)
- [numpy: Scientific Computing Tools For Python](https://www.numpy.org)
- [scipy: Scientific Tools for Python](https://www.scipy.org/)

## References

> T. C. Sutterley, T. Markus, T. A. Neumann, M. R. van den Broeke, J. M. van Wessem, and S. R. M. Ligtenberg,
> "Antarctic ice shelf thickness change from multimission lidar mapping", *The Cryosphere*,
> 13, 1801-1817, (2019). [doi: 10.5194/tc-13-1801-2019](https://doi.org/10.5194/tc-13-1801-2019)

## Download

The program homepage is:  
<https://github.com/pyTMD/timescale>

A zip archive of the latest version is available directly at:  
<https://github.com/pyTMD/timescale/archive/main.zip>

## Disclaimer

This package includes software developed at NASA Goddard Space Flight Center (GSFC) and the University of Washington Applied Physics Laboratory (UW-APL).
It is not sponsored or maintained by the Universities Space Research Association (USRA), AVISO or NASA.
The software is provided here for your convenience but *with no guarantees whatsoever*.

## Contributing

This project contains work and contributions from the [scientific community](./CONTRIBUTORS.md).
If you would like to contribute to the project, please have a look at the [contribution guidelines](./doc/source/getting_started/Contributing.rst), [open issues](https://github.com/pyTMD/timescale/issues) and [discussions board](https://github.com/pyTMD/timescale/discussions).

## License

The content of this project is licensed under the [Creative Commons Attribution 4.0 Attribution license](https://creativecommons.org/licenses/by/4.0/) and the source code is licensed under the [MIT license](LICENSE).
