Distribution metadata
---------------------

.. function:: metadata(distribution_name)

   Return the distribution metadata corresponding to the named
   distribution package as a :class:`PackageMetadata` instance.

   Raises :exc:`PackageNotFoundError` if the named distribution
   package is not installed in the current Python environment.

   Raises :exc:`MetadataNotFound` if a distribution package is
   present but no METADATA file is present.

.. class:: PackageMetadata

   A concrete implementation of the
   `PackageMetadata protocol <https://importlib-metadata.readthedocs.io/en/latest/api.html#importlib_metadata.PackageMetadata>`_.

   In addition to providing the defined protocol methods and attributes, subscripting
   the instance is equivalent to calling the :meth:`!get` method.

Every `Distribution Package <https://packaging.python.org/en/latest/glossary/#term-Distribution-Package>`_
includes some metadata, which you can extract using the :func:`!metadata` function::

    >>> wheel_metadata = metadata('wheel')  # doctest: +SKIP

The keys of the returned data structure name the metadata keywords, and
the values are returned unparsed from the distribution metadata::

    >>> wheel_metadata['Requires-Python']  # doctest: +SKIP
    '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

:class:`PackageMetadata` also presents a :attr:`!json` attribute that returns
all the metadata in a JSON-compatible form per :PEP:`566`::

    >>> wheel_metadata.json['requires_python']
    '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

The full set of available metadata is not described here.
See the PyPA `Core metadata specification <https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata>`_ for additional details.

.. versionchanged:: 3.15
   Previously and incidentally, if a METADATA file was missing from a distribution, an
   empty ``PackageMetadata`` would be returned, indistinguishable from
   an empty METADATA file. Now, a missing METADATA file triggers a
   ``MetadataNotFound`` exception.

.. versionchanged:: 3.10
   The ``Description`` is now included in the metadata when presented
   through the payload. Line continuation characters have been removed.

   The ``json`` attribute was added.


.. _version:
