# -*- coding: utf-8 -*-
__author__="Eduardo Torres Garcia"
__copyright__="Master's Degree 2020"
__version__="1.0.0"
__email__="Eduardo.Torres@cinvestav.mx"
__status__="Student"

import pathlib
import numpy as np
from numpy.ctypeslib import ndpointer
import ctypes
from ctypes import c_int
# Load the shared library into c types.
libname= pathlib.Path().absolute() / "libford.so"
c_lib = ctypes.CDLL(libname)

#Define return void pointer
c_lib.radixsort.restype= ctypes.c_void_p

#Define arguments
singlepp= ndpointer(dtype = np.int32, ndim=1, flags='C')
c_lib.ford.argtypes =[singlepp, ctypes.c_int]

#Define ndarray
matrix=[[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
x = np.arange(9, dtype = np.int32 )
c_lib.ford(x)

print(x)