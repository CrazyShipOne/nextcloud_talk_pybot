import ncbot.command.commander as commander

def command(plname, funcname, desc):
    def decorator(func):
        commander.register(plname, funcname, desc, func)
        return func

    return decorator
