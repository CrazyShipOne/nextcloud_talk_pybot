import ncbot.command.base as base

import openai
from ncbot.log_config import logger
from ncbot.plugins.utils.history import get_instance

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, ConversationChain

plugin_name = 'openai'
model_gpt_4 = 'gpt-4'
model_gpt_3 = 'gpt-3.5-turbo'

llm_gpt3 = ChatOpenAI(temperature=0.5, model_name=model_gpt_3)
llm_gpt4 = ChatOpenAI(temperature=0.5, model_name=model_gpt_4)


@base.command(plname=plugin_name, funcname='chat3',desc='Chat with Chatgpt using gpt-3.5-turbo model')
def chat3(userid, username, input):
    history_util = get_instance()
    history = history_util.get_memory(userid)
    llm_chain = ConversationChain(llm=llm_gpt3, memory = history, verbose=True)
    response = llm_chain.predict(input=input)
    history_util.save_memory(userid, history)
    return response


@base.command(plname=plugin_name, funcname='chat4',desc='Chat with Chatgpt using gpt-4 model')
def chat4(userid, username, input):
    history_util = get_instance()
    history = history_util.get_memory(userid)
    llm_chain = ConversationChain(llm=llm_gpt4, memory = history)
    response = llm_chain.predict(question=input, username=username)
    history_util.save_memory(userid, history)
    return response