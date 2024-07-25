def function(*positional_types, **keyword_types):
    def decorator(func):
        def inner(*args, **kwargs):
            N = len(positional_types)
            arg_count = 1
            for type_, arg in zip(positional_types, args):
                if arg_count > N:
                    break

                if not isinstance(arg, type_):
                    raise TypeError(f"positional argument {arg_count} of '{func.__name__}' expected type(s) {type_}, but got {type(arg)} instead")

                arg_count += 1

            for arg in kwargs.keys():
                if arg not in keyword_types.keys():
                    continue

                if not isinstance(kwargs[arg], keyword_types[arg]):
                    raise TypeError(f"keyword argument '{arg}' of '{func.__name__}' expected type(s) {keyword_types[arg]}, but got {type(kwargs[arg])} instead")

            return func(*args, **kwargs)
        return inner
    return decorator