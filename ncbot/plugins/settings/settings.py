from ncbot.utils.history import history_util
import ncbot.command.base as base


plugin_name = 'setting'


@base.command(plname=plugin_name, funcname='clear_history',desc='Delete all chat history.', remember_command=False)
def clear_history(userid, username, input):
    history_util.clear_memory(userid)
    return 'History cleared!'