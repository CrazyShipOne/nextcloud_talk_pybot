import time
from nc_helper import NCHelper
from config import Config
import traceback
from nc_chat import NCChat
import ncbot.command.commander as commander
from log_config import logger

cfg = Config()
nc_agent = NCHelper()

def start():
    
    while True:
        try:
            unread_chats = []
            unread_conversation = nc_agent.get_unread_conversation_list()
            logger.debug(f'found {len(unread_conversation)} unread conversations')
            for conversation in unread_conversation:
                chats = nc_agent.get_chat_list(conversation['token'],conversation['unreadMessages'])
                unread_chats += chats
                logger.debug(f'found {len(chats)} unread chats from token {conversation["token"]}')
            deal_unread_chats(unread_chats)

            
        except Exception as e:
            traceback.print_exc()
            logger.error(e)
        time.sleep(cfg.poll_interval_s)


def deal_unread_chats(unread_chats):
    unread_chats = sorted(unread_chats, key=lambda x:x['id'])
    for chat in unread_chats:
        chatC = NCChat(chat)
        if chatC.actor_name == cfg.username:
            skip_self_unread(chatC)
        else:
            try:
                commander.dispatch(chatC)
                send_response(chatC)
            except Exception as e:
                traceback.print_exc()
                logger.error(e)
        


def skip_self_unread(chat: NCChat):
    nc_agent.mark_chat_read(chat.conversation_token, chat.chat_id)


def send_response(chat: NCChat):
    if nc_agent.send_message(chat.conversation_token, chat.chat_id, chat.response):
        nc_agent.mark_chat_read(chat.conversation_token, chat.chat_id)


