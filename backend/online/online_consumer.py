from channels.generic.websocket import WebsocketConsumer
import json
from rest_framework.authtoken.models import Token
from asgiref.sync import async_to_sync
from channels.auth import login
import uuid
from online.models import SocketConnection

class OnlineConsumer(WebsocketConsumer):
    
    def connect(self):
        print('Connnect!!!')
        self.accept()
        self.send(text_data=json.dumps({ \
            'type': 'online:ping', \
            'payload': 'ping from server' \
            } \
        ))

    def disconnect(self, close_code):
        print('DISCONNECT!!! ONLINE')
        try:
            con = SocketConnection.objects.get(sid = self.sid).delete()
            profile = con.user
            con.delete()
            profile.update_online()            
        except:
            pass


    def receive(self, text_data):
        message = json.loads(text_data)
        if message['action'] == 'login':
            t = Token.objects.get(key=message['data']['token'])
            self.token = t.key
            self.sid = uuid.uuid1()
            profile = t.user.userprofile
            async_to_sync(login)(self.scope, profile)
            self.scope["session"].save()
            print('User login %s token %s' % (profile, message['data']['token']) )
    
            SocketConnection.create_if_not_exist( { \
                'user': profile, \
                'token': self.token, \
                'sid': self.sid, \
                'agent': message['data']['userAgent'] \
                })
            profile.update_online()

        