Hash algorithms
---------------

There is one constructor method named for each type of :dfn:`hash`.  All return
a hash object with the same simple interface. For example: use :func:`sha256`
to create a SHA-256 hash object. You can now feed this object with
:term:`bytes-like objects <bytes-like object>` (normally :class:`bytes`) using
the :meth:`update<hash.update>` method.  At any point you can ask it for the
:dfn:`digest` of the concatenation of the data fed to it so far using the
:meth:`digest()<hash.digest>` or :meth:`hexdigest()<hash.hexdigest>` methods.

To allow multithreading, the Python :term:`GIL` is released while computing a
hash supplied more than 2047 bytes of data at once in its constructor or
:meth:`.update<hash.update>` method.


.. index:: single: OpenSSL; (use in module hashlib)

Constructors for hash algorithms that are always present in this module are
:func:`md5`, :func:`sha1`, :func:`sha224`, :func:`sha256`, :func:`sha384`,
:func:`sha512`, :func:`sha3_224`, :func:`sha3_256`, :func:`sha3_384`,
:func:`sha3_512`, :func:`shake_128`, :func:`shake_256`, :func:`blake2b`, and
:func:`blake2s`.  These correspond to :data:`algorithms_guaranteed`.

Any of these may nonetheless be missing or blocked in unusual environments,
such as a rare "FIPS compliant" build of Python or when OpenSSL's "FIPS mode"
is configured to exclude some algorithms from its default provider.  Calling
the constructor of an algorithm that is unavailable raises :exc:`ValueError`.

Additional algorithms may also be available if your Python distribution's
:mod:`!hashlib` was linked against a build of OpenSSL that provides others.
Others *are not guaranteed available* on all installations and will only be
accessible by name via :func:`new`.  See :data:`algorithms_available`.

.. warning::

   Some algorithms have known hash collision weaknesses (including MD5 and
   SHA1). Refer to `Attacks on cryptographic hash algorithms`_ and the
   `hashlib-seealso`_ section at the end of this document.

.. versionadded:: 3.6
   SHA3 (Keccak) and SHAKE constructors :func:`sha3_224`, :func:`sha3_256`,
   :func:`sha3_384`, :func:`sha3_512`, :func:`shake_128`, :func:`shake_256`
   were added.
   :func:`blake2b` and :func:`blake2s` were added.

.. _hashlib-usedforsecurity:

.. versionchanged:: 3.9
   All hashlib constructors take a keyword-only argument *usedforsecurity*
   with default value ``True``. A false value allows the use of insecure and
   blocked hashing algorithms in restricted environments. ``False`` indicates
   that the hashing algorithm is not used in a security context, e.g. as a
   non-cryptographic one-way compression function.

.. versionchanged:: 3.9
   Hashlib now uses SHA3 and SHAKE from OpenSSL if it provides it.

.. versionchanged:: 3.12
   For any of the MD5, SHA1, SHA2, or SHA3 algorithms that the linked
   OpenSSL does not provide we fall back to a verified implementation from
   the `HACL\* project`_.

.. deprecated-removed:: 3.15 3.19
   The undocumented ``string`` keyword parameter in :func:`!_hashlib.new`
   and hash-named constructors such as :func:`!_md5.md5` is deprecated.
   Prefer passing the initial data as a positional argument for maximum
   backwards compatibility.

