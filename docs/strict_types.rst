.. _strict_types:

Strict Types
=============


.. module:: pyparcel

Strict types are used to **explicity** define how certain variables are to be packed.

**Note:** By default ``int``'s are packed as ``Int``, and ``float``'s are packed as ``Float``.

====================   ==========   ==================
Types                   # Bytes      Format Specifier
--------------------   ----------   ------------------
``Char``                 1            ``"c"``
``UnsignedChar``         1            ``"B"``
``SignedChar``           1            ``"b"``
``Short``                2            ``"h"``
``UnsignedShort``        2            ``"H"``
``Int``                  4            ``"i"``
``UnsignedInt``          4            ``"I"``
``Long``                 4            ``"l"``
``UnsignedLong``         4            ``"L"``
``LongLong``             8            ``"q"``
``UnsignedLongLong``     8            ``"Q"``
``Float``                4            ``"f"``
``Double``               8            ``"d"``
====================   ==========   ==================

Example
########
.. literalinclude:: ../examples/strict_class_example.py
    :language: python
    :lines: 1-9

Classes
########
.. autoclass:: Char
.. autoclass:: UnsignedChar
.. autoclass:: SignedChar
.. autoclass:: Short
.. autoclass:: UnsignedShort
.. autoclass:: Int
.. autoclass:: UnsignedInt
.. autoclass:: Long
.. autoclass:: UnsignedLong
.. autoclass:: LongLong
.. autoclass:: UnsignedLongLong
.. autoclass:: Float
.. autoclass:: Double
