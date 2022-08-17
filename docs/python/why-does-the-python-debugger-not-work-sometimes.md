---
author: ''
category: Python
date: '2022-08-13'
summary: ''
title: Why does the Python Debugger not Work Sometimes
---

## Why does the Python Debugger not Work Sometimes

Ever set a breakpoint with `breakpoint()` or `import ipdb; ipdb.set_trace()`- or perhaps you are using an IDE breakpoint - and the program does not break and enter the debugger?

Why is that? It is quite frustrating when trying to figure out the context and cause of a bug.

The reason is that the debugger relies on a shell or tty (teletype writer) access through "stdout/stderr/stdin" forwarding.

If `pdb` is entered in a process that does not have a `tty` available then it will just exit.

## Testing and PDB

Pytest I think had this problem because it captured `stdout`. To tell it to not capture `stdout` so that you can view the debugging consule use the `-s` flag

You also might encounter a problem with `pytest-xdist` - a package that distributes testing compute among cpu cores.

```
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/bdb.py:90: in trace_dispatch
    return self.dispatch_call(frame, arg)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <_pytest.debugging.pytestPDB._get_pdb_wrapper_class.<locals>.PytestPdbWrapper object at 0x114b41940>
frame = <frame at 0x7fb9852d0790, file '/Users/stephen/projects/forks/bitcart/api/schemes.py', line 29, code set_created>
arg = None

    def dispatch_call(self, frame, arg):
        """Invoke user function and return trace function for call event.
    
        If the debugger stops on this function call, invoke
        self.user_call(). Raise BdbQuit if self.quitting is set.
        Return self.trace_dispatch to continue tracing in this scope.
        """
        # XXX 'arg' is no longer used
        if self.botframe is None:
            # First call of dispatch since reset()
            self.botframe = frame.f_back # (CT) Note that this may also be None!
            return self.trace_dispatch
        if not (self.stop_here(frame) or self.break_anywhere(frame)):
            # No need to trace this function
            return # None
        # Ignore call events in generator except when stepping.
        if self.stopframe and frame.f_code.co_flags & GENERATOR_AND_COROUTINE_FLAGS:
            return self.trace_dispatch
        self.user_call(frame, arg)
>       if self.quitting: raise BdbQuit
E       bdb.BdbQuit

/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/bdb.py:135: BdbQuit
```

to fix that you can temporarily tell `pytest-xdist` to not distribute tests with the slave processes that don't have a tty.

Give it these flags:

    pytest -n0 --dist no


### Sources

https://github.com/pytest-dev/pytest/issues/390