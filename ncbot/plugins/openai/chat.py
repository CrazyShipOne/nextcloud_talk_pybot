import ncbot.command.base as base

import openai
from ncbot.log_config import logger

plug_in_name = 'openai'

messages_header = [
    {
        'role':'system',
        'content':'You are an intelligent AI assistant.'
    }
]

@base.command(plname=plug_in_name, funcname='chat',desc='Chat with Chatgpt')
def chat(input):
    messages = [] + messages_header
    messages.append({
        'role': 'user',
        'content': input
    })
    ret = ''
    try:
        reply = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages = messages)
        ret = reply.choices[0].message.content
    except Exception as e:
        logger.warn(f'call to openai chatcompletion api error: {e}')
        ret = 'Plugin error! Please try again.'
    return ret