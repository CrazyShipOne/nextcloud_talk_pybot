
from abc import abstractmethod
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.memory import ConversationBufferMemory, ChatMessageHistory
import ncbot.config as ncconfig
from ncbot.storages.storage_store import StorageStore

class MemoryHistoryUtil():
    storage_store:StorageStore = StorageStore.get_instance()

    def __init__(self):
        self.max_chat_history = ncconfig.cf.max_chat_history
        self.save_type = ncconfig.cf.save_type
    

    def _isStore(self):
        return self.max_chat_history != 0

  

    def clear_memory(self, userid):
        self.storage_store.remove_key(self._get_index_key(userid))


    def get_memory(self, userid):
        if not self._isStore():
            return None
        dict = self.storage_store.get_key_list_value(self._get_index_key(userid))
        if dict == None or len(dict) == 0:
            return ConversationBufferMemory()
        memory_dict = self.__dict_to_message(dict)
        history = ChatMessageHistory()
        history.messages = history.messages + memory_dict
        return ConversationBufferMemory(chat_memory=history)


    def save_memory(self, userid, history: ConversationBufferMemory):
        if not self._isStore():
            return
        chat_memory = history.chat_memory
        memory = self.__tuncate_memory(chat_memory)
        self.storage_store.set_key_list_value(self._get_index_key(userid), memory)


    def __tuncate_memory(self, history):
        memory_dict = self.__message_to_dict(history)
        if len(memory_dict) > self.max_chat_history * 2:
            memory_dict = memory_dict[2:]
        return memory_dict


    def _get_index_key(self, userid):
        return f'memory_{userid}'
    

    def __message_to_dict(self, history: ChatMessageHistory):
        return messages_to_dict(history.messages)
    

    def __dict_to_message(self, load_dict):
        return messages_from_dict(load_dict)
    

history_util = MemoryHistoryUtil()