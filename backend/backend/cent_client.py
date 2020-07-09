from cent import Client

from backend.settings import CENT_URL, CENT_KEY


class CentClient(object):

    def __init__(self):
        print('Init connection')
        self.con = Client(CENT_URL, api_key=CENT_KEY, timeout=1)

    def send(self,token,message):
        self.con.publish(token, message)

