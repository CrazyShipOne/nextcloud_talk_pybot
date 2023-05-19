import ncbot.command.commander as commander

def command(plname, funcname, desc, remember_command=True):
    def decorator(func):
        commander.register(plname, funcname, desc, func, remember_command)
        return func

    return decorator
