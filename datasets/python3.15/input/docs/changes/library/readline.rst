.. function:: get_pre_input_hook()

   Get the current pre-input hook function, or ``None`` if no pre-input hook
   function has been set.  This function only exists if Python was compiled
   for a version of the library that supports it.

   .. versionadded:: 3.15


.. _readline-completion:

Completion
----------

The following functions relate to implementing a custom word completion
function.  This is typically operated by the Tab key, and can suggest and
automatically complete a word being typed.  By default, Readline is set up
to be used by :mod:`rlcompleter` to complete Python identifiers for
the interactive interpreter.  If the :mod:`!readline` module is to be used
with a custom completer, a different set of word delimiters should be set.


.. function:: set_completer([function])

   Set or remove the completer function.  If *function* is specified, it will be
   used as the new completer function; if omitted or ``None``, any completer
   function already installed is removed.  The completer function is called as
   ``function(text, state)``, for *state* in ``0``, ``1``, ``2``, ..., until it
   returns a non-string value.  It should return the next possible completion
   starting with *text*.

   The installed completer function is invoked by the *entry_func* callback
   passed to :c:func:`!rl_completion_matches` in the underlying library.