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

    
    def checkEnv(self):
        if not self.base_url:
            raise Exception("NC_BASE_URL is not set")
        if not self.username:
            raise Exception("NC_USERNAME is not set")
        if not self.password:
            raise Exception("NC_PASSWORD is not set")
        self.only_new_message_after_start = bool(self.only_new_message_after_start)
