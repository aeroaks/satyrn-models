.. function:: fmax(x, y)

   Get the larger of two floating-point values, treating NaNs as missing data.

   When both operands are (signed) NaNs or zeroes, return ``nan`` and ``0``
   respectively and the sign of the result is implementation-defined, that
   is, :func:`!fmax` is not required to be sensitive to the sign of such
   operands (see Annex F of the C11 standard, §F.10.0.3 and §F.10.9.2).

   .. versionadded:: 3.15



----

.. function:: fmin(x, y)

   Get the smaller of two floating-point values, treating NaNs as missing data.

   When both operands are (signed) NaNs or zeroes, return ``nan`` and ``0``
   respectively and the sign of the result is implementation-defined, that
   is, :func:`!fmin` is not required to be sensitive to the sign of such
   operands (see Annex F of the C11 standard, §F.10.0.3 and §F.10.9.3).

   .. versionadded:: 3.15



----

.. function:: isnormal(x)

   Return ``True`` if *x* is a normal number, that is a finite
   nonzero number that is not a subnormal (see :func:`issubnormal`).
   Return ``False`` otherwise.

   .. versionadded:: 3.15



----

.. function:: issubnormal(x)

   Return ``True`` if *x* is a subnormal number, that is a finite
   nonzero number with a magnitude smaller than :data:`sys.float_info.min`.
   Return ``False`` otherwise.

   .. versionadded:: 3.15



----

.. function:: signbit(x)

   Return ``True`` if the sign of *x* is negative and ``False`` otherwise.

   This is useful to detect the sign bit of zeroes, infinities and NaNs.

   .. versionadded:: 3.15



----

Number-theoretic functions
--------------------------

For backward compatibility, the :mod:`!math` module provides also aliases of
the following functions from the :mod:`math.integer` module:

.. list-table::

   * - .. function:: comb(n, k)
          :no-typesetting:

       :func:`comb(n, k) <math.integer.comb>`
     - Number of ways to choose *k* items from *n* items without repetition
       and without order

   * - .. function:: factorial(n)
          :no-typesetting:

       :func:`factorial(n) <math.integer.factorial>`
     - *n* factorial

   * - .. function:: gcd(*integers)
          :no-typesetting:

       :func:`gcd(*integers) <math.integer.gcd>`
     - Greatest common divisor of the integer arguments

   * - .. function:: isqrt(n)
          :no-typesetting:

       :func:`isqrt(n) <math.integer.isqrt>`
     - Integer square root of a nonnegative integer *n*

   * - .. function:: lcm(*integers)
          :no-typesetting:

       :func:`lcm(*integers) <math.integer.lcm>`
     - Least common multiple of the integer arguments

   * - .. function:: perm(n, k)
          :no-typesetting:

       :func:`perm(n, k) <math.integer.perm>`
     - Number of ways to choose *k* items from *n* items without repetition
       and with order

.. versionadded:: 3.5
   The :func:`gcd` function.

.. versionadded:: 3.8
   The :func:`comb`, :func:`perm` and :func:`isqrt` functions.

.. versionadded:: 3.9
   The :func:`lcm` function.

.. versionchanged:: 3.9
   Added support for an arbitrary number of arguments in the :func:`gcd`
   function.
   Formerly, only two arguments were supported.

.. versionchanged:: 3.10
   Floats with integral values (like ``5.0``) are no longer accepted in the
   :func:`factorial` function.

.. soft-deprecated:: 3.15
   Use the :mod:`math.integer` functions instead of these aliases.

