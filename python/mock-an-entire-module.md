# How to mock an entire module (all functions and attrbutes)

Say for example you have a module that sends requests to a live system that you don't want running when you run tests.
The simple solution is to mock the entire module - although it is probably better to refactor that module and only change the function that is doing the sending out.
Even better would be to have a settings file for the environment to change the settings to a test server when in testing mode.

Nonetheless, we want to mock a module.

Say your module is called `sending_messages`, create a file called `mock_sending_messages.py`:

    from mock import Mock
    import sys
    import types

    module_name = 'sending_messages'
    mocked_module = types.ModuleType(module_name)
    sys.modules[module_name] = mocked_module

    # Do this for every function in that file
    mocked_module.my_function_name = Mock(name=module_name+'.my_function_name')

Save that and import it before you import the modules that use that module:

    from  mock_sending_messages import mocked_module

## Source

* [stackoverflow: Mock an entire module in python](https://stackoverflow.com/questions/41220803/mock-an-entire-module-in-python)