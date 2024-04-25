import ncbot.command.base as base

from ncbot.log_config import logger
from ncbot.utils.llm_util import get_user_chat_response
from ncbot.storages.storage_store import StorageStore

from langchain_google_genai import ChatGoogleGenerativeAI
import os

plugin_name = 'google_ai'
store = StorageStore.get_instance()
api_key = os.getenv('GOOGLE_API_KEY')
llm = ChatGoogleGenerativeAI(model_name='gemini-pro',api_key=api_key, convert_system_message_to_human=True)

@base.command(plname=plugin_name, funcname='chat',desc='Chat with model')
def chat(userid, username, input):
    global llm
    model_id = store.get_key(get_user_model_id_key(userid))
    if model_id and model_id != llm.model:
        llm = ChatGoogleGenerativeAI(model_id=model_id, api_key=api_key, convert_system_message_to_human=True)
    
    return get_user_chat_response(llm, userid, input)

@base.command(plname=plugin_name, funcname='set_model_id',desc='Set model_id, default is claude-3-opus-20240229')
def set_model(userid, username, input):
    store.set_key(get_user_model_id_key(userid), input)
    return f'model_id is set to {input}'

def get_user_model_id_key(userid):
    return f'{plugin_name}_{userid}_model_id'