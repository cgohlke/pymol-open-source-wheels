# setup.py for pymol-launcher

import sys
import subprocess
from setuptools import setup
from setuptools._distutils import ccompiler

with open('pymol.cpp', 'w') as fh:
    fh.write(
        """
#define WIN32_LEAN_AND_MEAN
#include <Python.h>
#include <windows.h>
#include <malloc.h>

int PyMOL_Main(int argc, char **argv)
{
    char* code = 
"import sys, os\n"
"sys.frozen = 1\n"
"import numpy\n"
"import __main__\n"
"__main__.pymol_launch = 2\n"
"__main__.pymol_argv = sys.argv\n"
"import pymol\n"
"pymol.finish_launching()\n";

    wchar_t **program_args = (wchar_t **)PyMem_Malloc(sizeof(wchar_t *) * (argc + 1)); 
    if (!program_args) { 
        Py_FatalError("out of memory"); 
    } 
    for (int i = 0; i < argc; i++) { 
        program_args[i] = (wchar_t *)PyMem_Malloc(sizeof(wchar_t) * (strlen(argv[i]) + 1)); 
        if (!program_args[i]) { 
            Py_FatalError("out of memory"); 
        } 
        program_args[i] = Py_DecodeLocale(argv[i], NULL);        
    }
    program_args[argc] = NULL;

    Py_SetProgramName(program_args[0]); 
    Py_Initialize();
    PySys_SetArgv(argc, program_args); 
    PyRun_SimpleString(code);
    Py_Finalize();
    return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    return PyMOL_Main(__argc, __argv);
}"""
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
    version="2.6",
    # install_requires=['pymol'],
    packages=[],
    libraries=[('', {'sources': []})],
    data_files=[('', ['PyMOL.exe'])],
)
