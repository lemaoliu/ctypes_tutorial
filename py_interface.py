import numpy.ctypeslib as ctl
import ctypes
import numpy as np


def print_array(libname, libdir, A, 3):
    libname = 'wrapper.so'
    libdir = './'
    lib=ctl.load_library(libname, libdir)
    py_print_array = lib.print_array
    py_print_array.argtypes = [ctl.ndpointer(np.float64, 
                                             flags='aligned, c_contiguous'), 
                               ctypes.c_int]
    A = np.array([1.4,2.6,3.0], dtype=np.float64)
    return py_print_array(A, 3)


