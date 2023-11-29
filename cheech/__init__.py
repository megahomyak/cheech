class _Action:
    def __init__(self, function):
        self.function = function

def action(function):
    return _Action(function)
