.. function:: getpass(prompt='Password: ', stream=None, *, echo_char=None)

   Prompt the user for a password without echoing.  The user is prompted using
   the string *prompt*, which defaults to ``'Password: '``.  On Unix, the
   prompt is written to the file-like object *stream* using the replace error
   handler if needed.  *stream* defaults to the controlling terminal
   (:file:`/dev/tty`) or if that is unavailable to ``sys.stderr`` (this
   argument is ignored on Windows).

   The *echo_char* argument controls how user input is displayed while typing.
   If *echo_char* is ``None`` (default), input remains hidden. Otherwise,
   *echo_char* must be a single printable ASCII character and each
   typed character is replaced by it. For example, ``echo_char='*'`` will
   display asterisks instead of the actual input.

   If echo free input is unavailable getpass() falls back to printing
   a warning message to *stream* and reading from ``sys.stdin`` and
   issuing a :exc:`GetPassWarning`.

   .. note::
      If you call getpass from within IDLE, the input may be done in the
      terminal you launched IDLE from rather than the idle window itself.

   .. note::
      On Unix systems, when *echo_char* is set, the terminal will be
      configured to operate in
      :manpage:`noncanonical mode <termios(3)#Canonical_and_noncanonical_mode>`.
      Common terminal control characters are supported:

      * :kbd:`Ctrl+A` - Move cursor to beginning of line
      * :kbd:`Ctrl+E` - Move cursor to end of line
      * :kbd:`Ctrl+K` - Kill (delete) from cursor to end of line
      * :kbd:`Ctrl+U` - Kill (delete) entire line
      * :kbd:`Ctrl+W` - Erase previous word
      * :kbd:`Ctrl+V` - Insert next character literally (quote)
      * :kbd:`Backspace`/:kbd:`DEL` - Delete character before cursor

      These shortcuts work by reading the terminal's configured control
      character mappings from termios settings.

   .. versionchanged:: 3.14
      Added the *echo_char* parameter for keyboard feedback.

   .. versionchanged:: 3.15
      When using non-empty *echo_char* on Unix, keyboard shortcuts (including
      cursor movement and line editing) are now properly handled using the
      terminal's control character configuration.
