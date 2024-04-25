from ncbot.nc_impl.nc_helper import NCHelper
from ncbot.nc_impl.nc_chat import NCChat
import os
import importlib.util
import logging
import subprocess
import inspect
logger = logging.getLogger(__name__)

nc_agent = NCHelper()

current_command = {}

plugin_path = 'ncbot/plugins'

user_command_cache = {}


class Command:

    def __init__(self, chat: NCChat):
        commandstr:str = chat.chat_message
        self.matched_func = False
        self.matched_plugin = False
        self.plname = None
        self.funcname = None
        self.value = None
        self.user_id = chat.user_id
        self.user_name = chat.user_name
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
        try:
            return self.func(self.user_id, self.user_name, self.value)
        except Exception as e:
            return 'Something wrong happened! Please try again later.'


def get_default_desc():
    desc = "You should type !Plugin:Function to talk with me.\n\nCurrent supported plugins are:\n"
    for key in current_command:
        desc += key+'\n'
    desc += "\nType !Plugin to see detail about plugin.\n"
    desc += "The last command will be remembered if capable, so you should not type the command first next time."
    return desc


def get_plugin_desc(plname):
    desc = 'Supported commands are:\n'
    plugin = current_command[plname]
    for key in plugin:
        desc += f'{key}: {plugin[key]["desc"]}\n'
    desc += f'type !{plname}:command input to use it.'
    return desc


def find_last_command(chat: NCChat):
    if not chat.chat_message.startswith('!'):
        key = f'command_{chat.user_id}'
        if key in user_command_cache:
            command = user_command_cache[key]
            chat.chat_message = f'{command} {chat.chat_message}'


def save_last_command(chat: NCChat, command: Command):
    if current_command[command.plname][command.funcname]['remember']:
        key = f'command_{chat.user_id}'
        user_command_cache[key] = f'!{command.plname}:{command.funcname}'
        return True
    return False


def dispatch(chat: NCChat):
    ret = 'test'
    #nc_agent.lock_conversation(chat.conversation_token)

    find_last_command(chat)
    command = Command(chat)
    if command.matched_func:
        ret = command.execute()
        if save_last_command(chat, command):
            ret += f'\n\n(The command !${command.plname}:{command.funcname} is remembered, type without command to continue use this function. Otherwize type other commands.)'
    elif command.matched_plugin:
        ret = get_plugin_desc(command.plname)
    else:
        ret = get_default_desc()
    #nc_agent.unlock_conversation(chat.conversation_token)
    chat.response = ret


def register(plname, funcname, desc, func, remember_command):
    if plname in current_command:
        current_command[plname][funcname] = {'desc':desc, 'func':func, 'remember':remember_command}
    else:
        current_command[plname] = {funcname: {'desc':desc, 'func':func, 'remember':remember_command}}


def load_plugin(path):
    for filename in os.listdir(path):
        tmppath = os.path.join(path, filename)
        if os.path.isfile(tmppath):
            if filename.endswith('.py') and not filename.startswith('__init'):
                spec = importlib.util.spec_from_file_location(filename[:-3], os.path.join(path, filename))
                module = importlib.util.module_from_spec(spec)
                logger.info(f'Loading plugin {module.__file__}')
                if verify_module_env(spec.origin):
                    install_required_lib(spec.origin)
                    try:
                        spec.loader.exec_module(module)
                    except Exception as ex:
                        logger.error(f'Load plugin {module.__file__} error: {ex}')
                else:
                    logger.warning(f'Invalid plugin {module.__file__}: no required variable lugins_required_module_version found')
        elif os.path.isdir(tmppath):
            load_plugin(tmppath)


def verify_module_env(spec_origin):
    parent_dir_path = os.path.dirname(spec_origin)
    requirements_txt_path = os.path.join(parent_dir_path, 'module_env.txt')
    if os.path.exists(requirements_txt_path):
        requirements = [line.strip() for line in open(requirements_txt_path, 'r')]
        for requirement in requirements:
            if os.environ.get(requirement) is None:
                logger.warning(f'Required env {requirement} is not set for plugin: {spec_origin}, not load')
                return False     
    else:
        logger.info(f'No module_env.txt found for {spec_origin}, deem doesn\'t required')
    return True


def install_required_lib(spec_origin):
    parent_dir_path = os.path.dirname(spec_origin)
    requirements_txt_path = os.path.join(parent_dir_path, 'requirements.txt')
    if os.path.exists(requirements_txt_path):
        process = subprocess.Popen(['pip', 'install', '-U','-r',requirements_txt_path], stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            logger.error(f'Install lib for {spec_origin} error:\n{error}')
            return False
        else:
            logger.info(f'Install lib for {spec_origin} success')
            # logger.debug(f'Install {spec_origin} output:\n{output}')
    else:
        logger.info(f'No requirements.txt found for {spec_origin}')
    return True
