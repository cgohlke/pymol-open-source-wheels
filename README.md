# Pymol-open-source wheels for Python on Windows

This repository provides unofficial binary wheels for [Pymol-open-source](https://github.com/schrodinger/pymol-open-source) for Python on Windows.

[PyMOL(tm)](https://pymol.org) is a visualization software for rendering and animating 3D molecular structures. PyMOL is a trademark of Schrodinger, LLC.

The files are unofficial (meaning: informal, unrecognized, personal, unsupported, no warranty, no liability, provided "as is") and made available for testing and evaluation purposes.

Source code changes, if any, have been submitted to the project maintainers or are included in the wheels.

## Installation

The wheels can be downloaded from the [Releases](https://github.com/cgohlke/pymol-open-source.whl/releases) page.

Install a wheel on the command line, for example for Python 3.13 64-bit:

    py.exe -3.13 -m pip install pymol-3.1.0-cp313-cp313-win_amd64.whl

Start the Pymol app using the ``pymol.exe`` executable in Python's script folder or from the command line:

    py.exe -3.13 -m pymol

The [Microsoft Visual C++ Redistributable packages for Visual Studio 2022](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170) is required to run the software.

The ``pymol-open-source`` package conflicts with the [``chempy``](https://pypi.org/project/chempy/) package. Only one library can be imported in a process.

## Release 2025.2.2

This release was built from the following source code:

- [Pymol-open-source](https://github.com/schrodinger/pymol-open-source/) 3.1.0 [master](https://github.com/schrodinger/pymol-open-source/commit/f51e58f6b08308c41c85b9d12a23231f49ca325a)
- [boost](https://www.boost.org/users/download/) 1.87.0
- [brotli](https://github.com/google/brotli) 1.1.0
- [bzip2](https://sourceware.org/pub/bzip2/) 1.0.8
- [freeglut](https://github.com/FreeGLUTProject/freeglut) 3.6.0
- [freetype](https://download.savannah.gnu.org/releases/freetype/) 2.13.3
- [glew](https://github.com/nigels-com/glew) 2.2.0
- [glm](https://github.com/g-truc/glm) 1.0.1
- [harfbuzz](https://github.com/harfbuzz/harfbuzz) 10.2.0
- [libpng](https://github.com/glennrp/libpng) 1.6.45
- [libxml2](https://gitlab.gnome.org/GNOME/libxml2) 2.12.9
- [libxslt](https://gitlab.gnome.org/GNOME/libxslt) 1.1.42
- [mmtf-cpp](https://github.com/rcsb/mmtf-cpp) 1.1.0
- [msgpack-cxx](https://github.com/msgpack/msgpack-c/tree/cpp_master) 6.1.0
- [VTK-m](https://gitlab.kitware.com/vtk/vtk-m) 1.9.0
- [win-iconv](https://github.com/OgreTransporter/win-iconv) master
- [zlib-ng](https://github.com/zlib-ng/zlib-ng) 2.2.3

## Build system

- [Windows Dev Kit](https://learn.microsoft.com/en-us/windows/arm/dev-kit/) 2023
- [Visual Studio](https://visualstudio.microsoft.com/vs/community/) 2022 Community 17.12
- [CPython](https://www.python.org/downloads/windows/) 3.10, 3.11, 3.12, 3.13
- [PyPy](https://www.pypy.org/download.html) 3.10

## Alternatives

Official binaries for PyMOL for Windows are available at [pymol.org](https://pymol.org).
