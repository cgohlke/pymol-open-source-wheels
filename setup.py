# setup.py for pymol-launcher

import subprocess
import sys

from setuptools import setup
from setuptools._distutils import ccompiler

with open('pymol.cpp', 'w') as fh:
    fh.write(
        """
#define WIN32_LEAN_AND_MEAN
#include <Python.h>
#include <windows.h>

int
PyMOL_Main(int argc, wchar_t **argv)
{
    PyStatus status;
    PyConfig config;

    PyConfig_InitPythonConfig(&config);
    status = PyConfig_SetArgv(&config, argc, argv);
    if (PyStatus_Exception(status)) {
        goto fail;
    }
    config.parse_argv = 0;
    status = PyConfig_SetString(&config, &config.run_module, L"pymol");
    if (PyStatus_Exception(status)) {
        goto fail;
    }
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto fail;
    }
    PyConfig_Clear(&config);
    return Py_RunMain();

fail:
    PyConfig_Clear(&config);
    if (PyStatus_IsExit(status)) {
        return status.exitcode;
    }
    assert(PyStatus_Exception(status));
    Py_ExitStatusException(status);
    return 0;
}

int WINAPI wWinMain(
    HINSTANCE hInstance,
    HINSTANCE hPrevInstance,
    LPWSTR lpCmdLine,
    int nCmdShow
)
{
    return PyMOL_Main(__argc, __wargv);
}
"""
    )

with open('pymol.rc', 'w') as fh:
    fh.write('IDI_MAIN_ICON ICON "PyMOL.ico"')

subprocess.run(['rc.exe', '/v', 'pymol.rc'])

compiler = ccompiler.new_compiler()
objects = compiler.compile(
    ['pymol.cpp'], include_dirs=[f'{sys.prefix}\\include']
)
compiler.link_executable(
    objects + ['pymol.res'],
    'PyMOL',
    output_dir='.',
    library_dirs=[f'{sys.prefix}\\libs'],
    libraries=[f'python3{sys.version_info[1]}'],
)

setup(
    name="pymol-launcher",
    version="3.2.0a0",
    # install_requires=['pymol'],
    packages=[],
    libraries=[('', {'sources': []})],
    data_files=[('', ['PyMOL.exe'])],
)
