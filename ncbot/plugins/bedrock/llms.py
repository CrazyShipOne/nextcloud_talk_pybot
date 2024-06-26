import ncbot.command.base as base

from ncbot.log_config import logger
from ncbot.utils.llm_util import get_user_chat_response
from ncbot.storages.storage_store import StorageStore

from langchain_aws import ChatBedrock

plugin_name = 'bedrock'
store = StorageStore.get_instance()
llm = ChatBedrock(model_id='anthropic.claude-3-haiku-20240307-v1:0')

@base.command(plname=plugin_name, funcname='chat',desc='Chat with model')
def chat(userid, username, input):
    global llm
    model_id = store.get_key(get_user_model_id_key(userid))
    if model_id and model_id != llm.model_id:
        llm = ChatBedrock(model_id=model_id)
    
    return get_user_chat_response(llm, userid, input)

@base.command(plname=plugin_name, funcname='set_model_id',desc='Set model_id, default is anthropic.claude-3-haiku-20240307-v1:0')
def set_model(userid, username, input):
    store.set_key(get_user_model_id_key(userid), input)
    return f'model_id is set to {input}'

def get_user_model_id_key(userid):
    return f'{plugin_name}_{userid}_model_id'