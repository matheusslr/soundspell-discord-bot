from utils.command_context import command_context

def command(name):
    def decorator(cls):
        command_context.register_strategy(name, cls)
        return cls
    return decorator
