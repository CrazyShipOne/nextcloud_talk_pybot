from nc_helper import NCHelper
from nc_chat import NCChat
import os
import importlib.util

nc_agent = NCHelper()

current_command = {}

plugin_path = 'ncbot/plugins'


def get_default_desc():
    desc = "You should type !Plugin:Function to talk with me.\nCurrent supported plugins are:\n"
    for key in current_command:
        desc += key+'\n'
    desc += "Type !Plugin to see detail about plugin"
    return desc


def get_plugin_desc(plname):
    desc = 'Supported commands are:\n'
    plugin = current_command[plname]
    for key in plugin:
        desc += f'{key}: {plugin[key]["desc"]}\n'
    desc += f'type !{plname}:command input to use it'
    return desc


def dispatch(chat: NCChat):
    ret = 'test'
    #nc_agent.lock_conversation(chat.conversation_token)

    command = Command(chat.chat_message)
    if command.matched_func:
        ret = command.execute()
    elif command.matched_plugin:
        ret = get_plugin_desc(command.plname)
    else:
        ret = get_default_desc()
    #nc_agent.unlock_conversation(chat.conversation_token)
    chat.response = ret


def register(plname, funcname, desc, func):
    if plname in current_command:
        current_command[plname][funcname] = {'desc':desc, 'func':func}
    else:
        current_command[plname] = {funcname: {'desc':desc, 'func':func}}


def load_plugin(path):
    for filename in os.listdir(path):
        tmppath = os.path.join(path, filename)
        if os.path.isfile(tmppath):
            if filename.endswith('.py') and not filename.startswith('__init'):
                spec = importlib.util.spec_from_file_location(filename[:-3], os.path.join(path, filename))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
        elif os.path.isdir(tmppath):
            load_plugin(tmppath)


class Command:

    def __init__(self, commandstr: str):
        self.matched_func = False
        self.matched_plugin = False
        self.plname = None
        self.funcname = None
        self.value = None
        if not commandstr.startswith('!'):
            return
        try:
            commandpair = commandstr.split(' ',1)
            commanddetail = commandpair[0][1:].split(':')
            self.plname = commanddetail[0]
            self.funcname = commanddetail[1]
            self.value = commandpair[1]
        except Exception:
            pass


        if self.plname in current_command:
                self.matched_plugin = True
                if self.funcname in current_command[self.plname]:
                    self.matched_func = True
                    self.func = current_command[self.plname][self.funcname]['func']       


    def execute(self):
        return self.func(self.value)
