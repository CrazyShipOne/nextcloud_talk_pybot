from ncbot.storages.storage_store import StorageStore
import ncbot.config as ncconfig
import redis
import json

conn = redis.Redis(host=ncconfig.cf.redis_host, port=ncconfig.cf.redis_port, db=ncconfig.cf.redis_db,password=ncconfig.cf.redis_pass)

class RedisStorage(StorageStore):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisStorage, cls).__new__(cls)
        return cls._instance

    def get_key(self, key):
        if conn.exists(key):
            return conn.get(key)

    def set_key(self, key, value):
        return conn.set(key, value)
    
    def set_key_list_value(self, key, value):
        for ele in value:
            conn.rpush(key, json.dumps(ele))
    
    def get_key_list_value(self, key):
        dict_range = conn.lrange(key,0, -1)
        dict = [json.loads(m.decode('utf-8')) for m in dict_range]
        return dict

    def remove_key(self, key):
        conn.delete(key)
