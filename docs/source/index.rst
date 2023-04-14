.. pyparcel documentation master file, created by
   sphinx-quickstart on Mon May 25 14:38:44 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _pyparcel: ./index.html
.. _pickle: https://docs.python.org/3/library/pickle.html
.. _struct: https://docs.python.org/3/library/struct.html



pyparcel
====================================

Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://travis-ci.org/najaco/pyparcel.svg?branch=master
    :target: https://travis-ci.org/najaco/pyparcel

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   install.rst
   api.rst

pyparcel_ is the simple and secure way to convert python objects to `bytestrings <https://docs.python.org/3/library/stdtypes.html#bytes>`_. When pyparcel_ performs ``pack`` on an object, it uses
recursive introspection on the objects variables and uses the struct_ module to pack each one in order (some additional rules may apply on dynamic data structures, e.g. ``str``, ``list``, etc.)
When pyparcel_ performs ``unpack`` on an data, it again performs recursive introspection and fills variables passed with what is apparent in the byte string.
By default, ``int`` s are stored as ``"i"`` with the standard size of 4 bytes, and ``float`` s  are stored as ``"f"`` with a standard size of 4 bytes.
If you would like to change how specific values are stored, see :ref:`strict types<strict_types>`.

Example
###################################################
.. literalinclude:: ../../examples/readme_example.py
    :language: python
    :lines: 1, 15-19

Comparison to other modules
############################

Comparison to pickle_
-------------------------
While pickle_ is great for *convenience*, it also lacks *security* because it allows the execution of *arbitrary functions*.
pyparcel_ is different because the user knows what objects are expected when unpacking the byte string. pyparcel_ recursively introspects the passed object and fills
the instance variables with what was given in the byte string.

Comparison to struct_
----------------------
struct_ is not as scalable as pyparcel_. struct_ requires you to specify the order and way data is packed,
and does not allow you to pack objects without deconstructing it first. While it may be faster during runtime, it requires the developer to change code in multiple places,
if they decide to customize the data they are passing. pyparcel_ acts as a *wrapper* around struct_, allowing objects to be converted to byte strings, since the *format specifier* for struct_
is decided at runtime.


