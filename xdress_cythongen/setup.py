import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'src'), np.get_include()]

ext_modules = [
    #Extension("xdress_cythongen.xdress_extra_types", ["xdress_cythongen/xdress_extra_types.pyx"], 
    #          include_dirs=incdirs, language="c++"),
    #Extension("xdress_cythongen.stlcontainers", ["xdress_cythongen/stlcontainers.pyx"], 
    #          include_dirs=incdirs, language="c++"),
    Extension("xdress_cythongen.hoover", ['src/hoover.cpp', "xdress_cythongen/hoover.pyx", ],
    	#'hoover/stlcontainers.pyx', 'hoover/xdress_extra_types.pyx'],
    	include_dirs=incdirs, language="c++")
    ]

setup(  
  name = 'xdress_cythongen',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['xdress_cythongen']
)
