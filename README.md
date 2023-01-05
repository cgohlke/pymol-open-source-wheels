# Pymol-open-source wheels for Python on Windows 

This repository provides unofficial binary wheels for [Pymol-open-source](https://github.com/schrodinger/pymol-open-source) for Python on Windows.

[PyMOL(tm)](https://pymol.org) is a visualization software for rendering and animating 3D molecular structures. PyMOL is a trademark of Schrodinger, LLC.

The files are unofficial (meaning: informal, unrecognized, personal, unsupported, no warranty, no liability, provided "as is") and made available for testing and evaluation purposes.

Source code changes, if any, have been submitted to the project maintainers or are included in the wheels.

## Installation

The wheels can be downloaded from the [Releases](https://github.com/cgohlke/pymol-open-source.whl/releases) page.

Install a wheel on the command line (e.g., for Python 3.11 64-bit):

    $ py.exe -3.11 -m pip install pymol-2.6.0a0-cp311-cp311-win_amd64.whl
    
Start the Pymol app using the ``pymol.exe`` executable in Python's script folder or from the command line:

    $ py.exe -3.11 -m pymol

The [Microsoft Visual C++ Redistributable packages for Visual Studio 2022](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170) is required to run the software.

The ``pymol-open-source`` package conflicts with the [``chempy``](https://pypi.org/project/chempy/) package. Only one library can be imported in a process.

## Release 2023.1.4

This release has been built from the following source code:

- [Pymol-open-source](https://github.com/schrodinger/pymol-open-source/) 2.6.0a0 [f70c533](https://github.com/schrodinger/pymol-open-source/commit/f70c533d015b1017a6aa77a05c644b70725c4e23)
- [boost](https://www.boost.org/users/download/) 1.81.0
- [brotli](https://github.com/google/brotli) 1.0.9
- [bzip2](https://sourceware.org/pub/bzip2/) 1.0.8
- [freeglut](https://github.com/FreeGLUTProject/freeglut) 3.4.0
- [freetype](https://download.savannah.gnu.org/releases/freetype/) 2.12.1
- [glew](https://github.com/nigels-com/glew) 2.2.0
- [glm](https://github.com/g-truc/glm) 0.9.9.8
- [harfbuzz](https://github.com/harfbuzz/harfbuzz) 5.3.1
- [libpng](https://github.com/glennrp/libpng) 1.6.39
- [libxml2](https://gitlab.gnome.org/GNOME/libxml2) 2.10.3
- [libxslt](https://gitlab.gnome.org/GNOME/libxslt) 1.1.37
- [mmtf-cpp](https://github.com/rcsb/mmtf-cpp) 1.1.0
- [msgpack-cxx](https://github.com/msgpack/msgpack-c/tree/cpp_master) 4.1.3
- [VTK-m](https://gitlab.kitware.com/vtk/vtk-m) 1.9.0
- [win-iconv](https://github.com/OgreTransporter/win-iconv) master
- [zlib](https://github.com/madler/zlib) 1.2.13

## Build system

- [Windows Dev Kit](https://learn.microsoft.com/en-us/windows/arm/dev-kit/) 2023
- [Visual Studio](https://visualstudio.microsoft.com/vs/community/) 2022 Community 17.4
- [CPython](https://www.python.org/downloads/windows/) 3.8, 3.9, 3.10, 3.11
- [PyPy](https://www.pypy.org/download.html) 3.9

## Alternatives

Official binaries for PyMOL for Windows are available at [pymol.org](https://pymol.org).
