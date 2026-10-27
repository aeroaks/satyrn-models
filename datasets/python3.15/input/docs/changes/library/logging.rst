.. function:: basicConfig(**kwargs)

   Does basic configuration for the logging system by either creating a
   :class:`StreamHandler` with a default :class:`Formatter`
   or using the  given *formatter* instance, and adding it to the
   root logger. The functions :func:`debug`, :func:`info`, :func:`warning`,
   :func:`error` and :func:`critical` will call :func:`basicConfig` automatically
   if no handlers are defined for the root logger.

   This function does nothing if the root logger already has handlers
   configured, unless the keyword argument *force* is set to ``True``.

   .. note:: This function should be called from the main thread
      before other threads are started. In versions of Python prior to
      2.7.1 and 3.2, if this function is called from multiple threads,
      it is possible (in rare circumstances) that a handler will be added
      to the root logger more than once, leading to unexpected results
      such as messages being duplicated in the log.

   The following keyword arguments are supported.

   .. tabularcolumns:: |l|L|

   +--------------+---------------------------------------------+
   | Format       | Description                                 |
   +==============+=============================================+
   | *filename*   | Specifies that a :class:`FileHandler` be    |
   |              | created, using the specified filename,      |
   |              | rather than a :class:`StreamHandler`.       |
   +--------------+---------------------------------------------+
   | *filemode*   | If *filename* is specified, open the file   |
   |              | in this :ref:`mode <filemodes>`. Defaults   |
   |              | to ``'a'``.                                 |
   +--------------+---------------------------------------------+
   | *format*     | Use the specified format string for the     |
   |              | handler. Defaults to attributes             |
   |              | ``levelname``, ``name`` and ``message``     |
   |              | separated by colons.                        |
   +--------------+---------------------------------------------+
   | *datefmt*    | Use the specified date/time format, as      |
   |              | accepted by :func:`time.strftime`.          |
   +--------------+---------------------------------------------+
   | *style*      | If *format* is specified, use this style    |
   |              | for the format string. One of ``'%'``,      |
   |              | ``'{'`` or ``'$'`` for :ref:`printf-style   |
   |              | <old-string-formatting>`,                   |
   |              | :meth:`str.format` or                       |
   |              | :class:`string.Template` respectively.      |
   |              | Defaults to ``'%'``.                        |
   +--------------+---------------------------------------------+
   | *level*      | Set the root logger level to the specified  |
   |              | :ref:`level <levels>`.                      |
   +--------------+---------------------------------------------+
   | *stream*     | Use the specified stream to initialize the  |
   |              | :class:`StreamHandler`. Note that this      |
   |              | argument is incompatible with *filename* -  |
   |              | if both are present, a ``ValueError`` is    |
   |              | raised.                                     |
   +--------------+---------------------------------------------+
   | *handlers*   | If specified, this should be an iterable of |
   |              | already created handlers to add to the root |
   |              | logger. Any handlers which don't already    |
   |              | have a formatter set will be assigned the   |
   |              | default formatter created in this function. |
   |              | Note that this argument is incompatible     |
   |              | with *filename* or *stream* - if both       |
   |              | are present, a ``ValueError`` is raised.    |
   +--------------+---------------------------------------------+
   | *force*      | If this keyword argument is specified as    |
   |              | true, any existing handlers attached to the |
   |              | root logger are removed and closed, before  |
   |              | carrying out the configuration as specified |
   |              | by the other arguments.                     |
   +--------------+---------------------------------------------+
   | *encoding*   | If this keyword argument is specified along |
   |              | with *filename*, its value is used when the |
   |              | :class:`FileHandler` is created, and thus   |
   |              | used when opening the output file.          |
   +--------------+---------------------------------------------+
   | *errors*     | If this keyword argument is specified along |
   |              | with *filename*, its value is used when the |
   |              | :class:`FileHandler` is created, and thus   |
   |              | used when opening the output file. If not   |
   |              | specified, the value 'backslashreplace' is  |
   |              | used. Note that if ``None`` is specified,   |
   |              | it will be passed as such to :func:`open`,  |
   |              | which means that it will be treated the     |
   |              | same as passing 'errors'.                   |
   +--------------+---------------------------------------------+
   | *formatter*  | If specified, set this formatter instance   |
   |              | (see :ref:`formatter-objects`)              |
   |              | for all involved handlers.                  |
   |              | If not specified, the default is to create  |
   |              | and use an instance of                      |
   |              | :class:`logging.Formatter` based on         |
   |              | arguments *format*, *datefmt* and *style*.  |
   |              | When *formatter* is specified together with |
   |              | any of the three arguments *format*,        |
   |              | *datefmt* and *style*, a ``ValueError`` is  |
   |              | raised to signal that these arguments would |
   |              | lose meaning otherwise.                     |
   +--------------+---------------------------------------------+

   .. versionchanged:: 3.2
      The *style* argument was added.

   .. versionchanged:: 3.3
      The *handlers* argument was added. Additional checks were added to
      catch situations where incompatible arguments are specified (e.g.
      *handlers* together with *stream* or *filename*, or *stream*
      together with *filename*).

   .. versionchanged:: 3.8
      The *force* argument was added.

   .. versionchanged:: 3.9
      The *encoding* and *errors* arguments were added.

   .. versionchanged:: 3.15
      The *formatter* argument was added.
