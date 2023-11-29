from argparse import ArgumentParser

class WithDefault:
    def __init__(self, argname, default_value):
        self.argname = argname
        self.default_value = default_value

def require(*argnames):
    argparser = ArgumentParser()
    plain_argnames = []
    for argname in argnames:
        if isinstance(argname, WithDefault):
            plain_argnames.append(argname.argname)
            argparser.add_argument("-" + argname.argname, default=argname.default_value)
        elif isinstance(argname, str):
            plain_argnames.append(argname)
            argparser.add_argument("-" + argname)
        else:
            raise TypeError(f"encountered an argument name of an incompatible type {type(argname)}")
    args = argparser.parse_args()
    return [
        getattr(args, plain_argname)
        for plain_argname in plain_argnames
    ]
