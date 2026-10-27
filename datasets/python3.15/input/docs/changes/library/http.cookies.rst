.. method:: BaseCookie.js_output(attrs=None)

   Return an embeddable JavaScript snippet, which, if run on a browser which
   supports JavaScript, will act the same as if the HTTP headers was sent.

   The meaning for *attrs* is the same as in :meth:`output`.

   .. deprecated-removed:: 3.15 3.19
      This method generates a JavaScript snippet to set cookies in the browser,
      which is no longer considered a standard or recommended approach.
      Use :meth:`~http.cookies.BaseCookie.output` instead to generate HTTP
      headers.



----

.. method:: Morsel.js_output(attrs=None)

   Return an embeddable JavaScript snippet, which, if run on a browser which
   supports JavaScript, will act the same as if the HTTP header was sent.

   The meaning for *attrs* is the same as in :meth:`output`.

   .. deprecated-removed:: 3.15 3.19
      This method generates a JavaScript snippet to set cookies in the browser,
      which is no longer considered a standard or recommended approach.
      Use :meth:`~http.cookies.Morsel.output` instead to generate HTTP
      headers.

