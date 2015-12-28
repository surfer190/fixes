# Documentation - Using Pydoc

You use pydoc in the same way you use `man` on linux

Example:

  pydoc raw_input

Output:

    raw_input(...)
      raw_input([prompt]) -> string
      
      Read a string from standard input.  The trailing newline is stripped.
      If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
      On Unix, GNU readline is used if enabled.  The prompt string, if given,
      is printed without a trailing newline before reading.