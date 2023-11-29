from argparse import ArgumentParser as _ArgumentParser

_NOT_SPECIFIED = object()

class Arg:
    def __init__(self, argname, *, default=_NOT_SPECIFIED, converter=lambda x: x):
        self.name = argname
        self.default = default
        self.converter = converter

def require(*args):
    converted_args = []
    for arg in args:
        if isinstance(arg, str):
            arg = Arg(arg)
        converted_args.append(arg)
    args = converted_args
    argparser = _ArgumentParser()
    for arg in args:
        kwargs = {}
        if arg.default is _NOT_SPECIFIED:
            kwargs["required"] = True
        else:
            kwargs["default"] = arg.default
        argparser.add_argument("--" + arg.name, **kwargs)
    input_values = argparser.parse_args()
    return [
        arg.converter(getattr(input_values, arg.name))
        for arg in args
    ]
