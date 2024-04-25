import ncbot.config as ncconfig
import importlib
from abc import abstractmethod

class StorageStore():
    @abstractmethod
    def get_instance():
        match ncconfig.cf.save_type:
            case 'memory':
                module = importlib.import_module('ncbot.storages.in_memory_storage')
                return module.InMemoryStorage()
            case 'redis':
                module = importlib.import_module('ncbot.storages.redis_storage')
                return module.RedisStorage()
    
    def set_key(self, key, value):
        pass
    
    def get_key(self, key):
        pass
    
    def set_key_list_value(self, key, value):
        pass
    
    def get_key_list_value(self, key):
        pass
    
    def remove_key(self, key):
        pass
