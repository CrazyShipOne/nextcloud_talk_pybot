from ncbot.storages.storage_store import StorageStore

class InMemoryStorage(StorageStore):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InMemoryStorage, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.storage = {}

    def get_key(self, key):
        if key not in self.storage:
            return None
        return self.storage.get(key)

    def set_key(self, key, value):
        if key:
            self.storage[key] = value
            
    def get_key_list_value(self, key):
        return self.get_key(key)
    
    def set_key_list_value(self, key, value):
        self.set_key(key, value)

    def remove_key(self, key):
        self.storage.pop(key, None)
        return