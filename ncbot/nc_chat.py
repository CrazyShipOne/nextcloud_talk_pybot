import re

regex_comment = r'^\{.*\}$'

class NCChat:

    def __init__(self, chat) -> None:
        self.conversation_token = chat['token']
        self.chat_id = chat['id']
        self.chat_message = chat['message']
        self.dealable = self.check_comment_type_available(self.chat_message)
        self.response = None
        self.user_id = chat['actorId']
        self.user_name = chat['actorDisplayName']
        self.chat_type = chat['actorType']


    def check_comment_type_available(self, comment:str):
        return not re.match(regex_comment, comment)