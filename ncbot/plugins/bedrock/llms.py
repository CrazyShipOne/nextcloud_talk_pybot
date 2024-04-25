import ncbot.command.base as base

from ncbot.log_config import logger
from ncbot.utils.history import history_util
from ncbot.prompt_config import default_history_template
from ncbot.storages.storage_store import StorageStore

from langchain_aws import ChatBedrock
from langchain.chains import ConversationChain

plugin_name = 'bedrock'
store = StorageStore.get_instance()
llm = ChatBedrock(model_id='anthropic.claude-3-haiku-20240307-v1:0')

@base.command(plname=plugin_name, funcname='chat',desc='Chat with model')
def chat(userid, username, input):
    global llm
    history = history_util.get_memory(userid)
    model_id = store.get_key(get_user_model_id_key(userid))
    if model_id and model_id != llm.model_id:
        llm = ChatBedrock(model_id=model_id)
    llm_chain = ConversationChain(llm=llm, memory = history, verbose=False, prompt=default_history_template)
    response = llm_chain.predict(input=input)
    history_util.save_memory(userid, history)
    return response

@base.command(plname=plugin_name, funcname='set_model_id',desc='Set model_id, default is anthropic.claude-3-haiku-20240307-v1:0')
def set_model(userid, username, input):
    store.set_key(get_user_model_id_key(userid), input)
    return f'model_id is set to {input}'

def get_user_model_id_key(userid):
    return f'{plugin_name}_{userid}_model_id'