import os
import time

class Config():

    def __new__(cls):
        if not  hasattr(cls, 'instance'):
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance


    def __init__(self) -> None:
        self.base_url = os.getenv('NC_BASE_URL')
        self.username = os.getenv('NC_USERNAME')
        self.password = os.getenv('NC_PASSWORD')
        self.poll_interval_s = int(os.getenv('POLL_INTERVAL', default=5))
        self.only_new_message_after_start = os.getenv('ONLY_NEW')
        self.start_time = int(time.time())
        self.max_message = int(os.getenv('MAX_MESSAGE', default=10))

        #plugins
        self.save_type = os.getenv('HISTORY_STORAGE','memory')
        self.max_chat_history = int(os.getenv('MAX_CHAT_HISTORY',0))

        
        self.redis_host = os.getenv('REDIS_HOST')
        self.redis_port = int(os.getenv('REDIS_PORT',6379))
        self.redis_pass = os.getenv('REDIS_PASS',None)
        self.redis_db = int(os.getenv('REDIS_DB',0))

    
    def checkEnv(self):
        if not self.base_url:
            raise Exception("NC_BASE_URL is not set")
        if not self.username:
            raise Exception("NC_USERNAME is not set")
        if not self.password:
            raise Exception("NC_PASSWORD is not set")
        self.only_new_message_after_start = bool(self.only_new_message_after_start)


cf = Config()
