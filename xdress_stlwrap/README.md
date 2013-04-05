# xdress_stlwrap

This is a simple example of how to use xdress stlwrap.

## Build and test

    xdress -v
    touch xdress_stlwrap/__init__.py
    python setup.py build_ext -i
    nosetests

## Use

$ ipython

In [1]: import xdress_stlwrap.stlcontainers as x

In [2]: x.
x.MapIntDouble  x.SetUInt       x.XDStr         x.collections   x.dtypes        x.np            x.xd_str        
