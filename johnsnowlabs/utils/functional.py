from typing import Callable, Dict


def extract_callee_args_as_kwargs(func: Callable) -> Dict[str, any]:
    """
    Extract all parameters a function was called with during execution time as kwarg dict.
    Call this from inside a function and this returns all parameters the function was given at run time.
    Handy to reduce boilerplate on funcs with many args
    :param func: The function to get kwargs from.  A function should pass itself as parameter when calling this
    :return: value kwargs of the func at the time of calling the extract_args_as_kwargs function
    """
    import inspect

    # Get the names of the functions parameters
    param_names = list(
        map(lambda x: x.name, inspect.signature(func).parameters.values())
    )
    # We go 2 frame up, one for the dict comprehension, and one for extract_args_as_kwargs func itself
    kwargs = {
        n: inspect.getouterframes(inspect.currentframe())[2].frame.f_locals[n]
        for n in param_names
    }
    return kwargs
