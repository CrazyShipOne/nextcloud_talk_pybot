import ncbot.command.base as base

from ncbot.log_config import logger
from ncbot.storages.storage_store import StorageStore

from langchain_openai import ChatOpenAI
from ncbot.utils.llm_util import get_user_chat_response


plugin_name = 'openai'
store = StorageStore.get_instance()
model_gpt_3 = 'gpt-3.5-turbo'

llm = ChatOpenAI(temperature=0.7, model_name=model_gpt_3)


@base.command(plname=plugin_name, funcname='chat3',desc='Chat with Chatgpt')
def chat3(userid, username, input):
    global llm
    model_name = store.get_key(get_user_model_id_key(userid))
    if model_name and model_name != llm.model_name:
        llm = ChatOpenAI(azure_deployment=model_name)
    return get_user_chat_response(llm, userid, input)


@base.command(plname=plugin_name, funcname='set_model_name',desc='Set model name, default is gpt-3.5-turbo')
def set_model(userid, username, input):
    store.set_key(get_user_model_id_key(userid), input)
    return f'Model name is set to {input}'

def get_user_model_id_key(userid):
    return f'{plugin_name}_{userid}_model_name'