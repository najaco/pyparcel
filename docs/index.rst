.. pyparcel documentation master file, created by
   sphinx-quickstart on Mon May 25 14:38:44 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyparcel
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   strict_types.rst

pyparcel allows you to easily converted your python object to and from a byte string format.

Example `[src] <../examples/readme_example.py>`_
###################################################
.. literalinclude:: ../examples/readme_example.py
    :linenos:
    :language: python
    :lines: 1, 11-19

pyparcel is great for networking with python. It provides an alternative method to the `struct <https://docs.python.org/3/library/struct.html>`_ module
by not requiring users to have to redefine how an object is *packed*. This is because it's the objects packing definition is defined through recursion at runtime.
You can specify how types are stored by defining them as strict types. 