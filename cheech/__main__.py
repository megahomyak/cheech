from typing import Optional, Tuple
from appdirs import user_config_dir
import os
import runpy
from . import _Action
import sys

class FunctionNameCollision(Exception): pass
class FunctionNotFound(Exception): pass
class RepeatingKeywordArgument(Exception): pass

function_name, *argument_strings = sys.argv[1:]

def split_by_equals_sign_if_not_escaped(string) -> Tuple[Optional[str], str]:
    try:
        equals_sign_index = string.index("=")
    except ValueError:
        return (None, string)
    if equals_sign_index == 0 or string[equals_sign_index - 1] == "\\":
        return (None, string)
    return (string[:equals_sign_index], string[equals_sign_index + 1:])

args = []
kwargs = {}
for argument_string in argument_strings:
    parts = NOT_ESCAPED_EQUALS_SIGN.split(argument_string, maxsplit=1)
    try:
        name, value = parts
        if name in kwargs:
            raise RepeatingKeywordArgument()
        kwargs[name] = value
    except ValueError:
        [value] = parts
        args.append(value)

config_path = user_config_dir(appname="cheech", appauthor=False)
programs_path = os.path.join(config_path, "programs")

functions = {}

for file_name in os.listdir(programs_path):
    file_path = os.path.join(programs_path, file_name)
    file_globals = runpy.run_path(file_path)
    for name, object_ in file_globals.items():
        if isinstance(object_, _Action):
            if name in functions:
                raise FunctionNameCollision()
            functions[name] = object_.function

try:
    function = functions[function_name]
except KeyError:
    raise FunctionNotFound()

function(*args, **kwargs)
