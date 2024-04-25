import ncbot.command.base as base

from ncbot.log_config import logger
from ncbot.utils.history import history_util

from langchain_openai import ChatOpenAI
from ncbot.prompt_config import default_history_template
from langchain.chains import ConversationChain

plugin_name = 'openai'
model_gpt_4 = 'gpt-4'
model_gpt_3 = 'gpt-3.5-turbo'

llm_gpt3 = ChatOpenAI(temperature=0.5, model_name=model_gpt_3)
llm_gpt4 = ChatOpenAI(temperature=0.5, model_name=model_gpt_4)


@base.command(plname=plugin_name, funcname='chat3',desc='Chat with Chatgpt using gpt-3.5-turbo model')
def chat3(userid, username, input):
    history = history_util.get_memory(userid)
    llm_chain = ConversationChain(llm=llm_gpt3, memory = history, verbose=False, prompt=default_history_template)
    response = llm_chain.predict(input=input)
    history_util.save_memory(userid, history)
    return response


@base.command(plname=plugin_name, funcname='chat4',desc='Chat with Chatgpt using gpt-4 model')
def chat4(userid, username, input):
    history = history_util.get_memory(userid)
    llm_chain = ConversationChain(llm=llm_gpt4, memory = history, verbose=False, prompt=default_history_template)
    response = llm_chain.predict(input=input)
    history_util.save_memory(userid, history)
    return response