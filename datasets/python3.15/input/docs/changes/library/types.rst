.. class:: FrameLocalsProxyType

   The type of frame locals proxy objects, as found on the
   :attr:`frame.f_locals` attribute.

   .. versionadded:: 3.15

   .. seealso:: :pep:`667`



----

.. class:: LazyImportType

   The type of lazy import proxy objects. These objects are created when a
   module is lazily imported and serve as placeholders until the module is
   actually accessed. This type can be used to detect lazy imports
   programmatically.

   .. versionadded:: 3.15

   .. seealso:: :pep:`810`

   .. method:: resolve()

      Reify the lazy import and return the "real" object being imported.

