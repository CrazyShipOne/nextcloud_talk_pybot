import request_util as rutil
import nc_constants
import ncbot.config as ncconfig


class NCHelper:

    base_endpoint_v4 = '/ocs/v2.php/apps/spreed/api/v4'
    base_endpoint_v1 = '/ocs/v2.php/apps/spreed/api/v1'


    def __new__(cls):
        if not  hasattr(cls, 'instance'):
            cls._instance = super(NCHelper, cls).__new__(cls)
        return cls._instance
    

    def get_unread_conversation_list(self):
        params = {'noStatusUpdate':0, 'includeStatus':True}
        if ncconfig.cf.only_new_message_after_start:
            params['modifiedSince'] = ncconfig.cf.start_time
        mesg = rutil.get_response(self.final_url_v4('room'), params=params)
        unread = []
        for ele in mesg['ocs']['data']:
            if ele['unreadMessages'] > 0:
                unread.append(ele)
        return unread
    

    def get_chat_list(self, token, mesg_count=0):
        limit = mesg_count if mesg_count < ncconfig.cf.max_message else ncconfig.cf.max_message
        params = {
            'lookIntoFuture':nc_constants.chat_history,
            'limit':limit,
            'setReadMarker':0,
            'includeLastKnown':1,
        }
        mesg = rutil.get_response(self.final_url_v1(f'/chat/{token}'), params=params)
        return mesg['ocs']['data']


    def lock_conversation(self, token):
        data = {'state':nc_constants.conversation_read_only}
        rutil.put_response(self.final_url_v4(f'/room/{token}/read-only'), data)


    def unlock_conversation(self, token):
        data = {'state':nc_constants.conversation_read_write}
        rutil.put_response(self.final_url_v4(f'/room/{token}/read-only'), data)

    
    def send_message(self, token, chatid, comment, message,user_id, direct_reply = False):
        data = {}
        if direct_reply :
            data['message'] = comment
            data['replyTo'] = chatid
        else:
            data['message'] = f'Reponse to "{message}" is:\n\n' + comment
        data['message'] = f'@"{user_id}" \n'+data['message']
        response = rutil.post_response(self.final_url_v1(f'/chat/{token}'), data)
        return response != None
    

    def mark_chat_read(self, token, id):
        data = {'lastReadMessage':id}
        response = rutil.post_response(self.final_url_v1(f'/chat/{token}/read'), data)
        return response != None


    def final_url_v4(self, path):
        return self.base_endpoint_v4 + rutil.check_uri_prefix(path)

    def final_url_v1(self, path):
        return self.base_endpoint_v1 + rutil.check_uri_prefix(path)
