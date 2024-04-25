import ncbot.command.base as base

from ncbot.log_config import logger
from ncbot.storages.storage_store import StorageStore

from langchain_openai import AzureChatOpenAI
from ncbot.utils.llm_util import get_user_chat_response


plugin_name = 'azure_openai'
store = StorageStore.get_instance()
llm = AzureChatOpenAI(temperature=0.7)


@base.command(plname=plugin_name, funcname='chat',desc='Chat with Azure OpenAI model')
def chat(userid, username, input):
    global llm
    model_name = store.get_key(get_user_model_id_key(userid))
    if model_name and model_name != llm.deployment_name:
        llm = AzureChatOpenAI(azure_deployment=model_name)
    return get_user_chat_response(llm, userid, input)


@base.command(plname=plugin_name, funcname='set_de_name',desc='Set deployment name, default is from env: AZURE_OPENAI_CHAT_DEPLOYMENT_NAME')
def set_model(userid, username, input):
    store.set_key(get_user_model_id_key(userid), input)
    return f'Deployment name is set to {input}'

def get_user_model_id_key(userid):
    return f'{plugin_name}_{userid}_model_name'