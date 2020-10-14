from cent import Client

from backend.settings import CENT_URL, CENT_KEY

class CentClient(object):

    def __init__(self):
        self.con = Client(CENT_URL, api_key=CENT_KEY, timeout=1)

    def send(self,token,message):
        try:
            self.con.publish(token, message)
        except:
            print('Centrifugo does not work!')
        #print(" HISTORY OF MESSAGES : ", self.con.history(token))

