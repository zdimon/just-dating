from django.db import models

from account.models import UserProfile

class SocketConnection(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=250, db_index=True, null=True)
    sid = models.CharField(max_length=250, db_index=True, null=True, unique=True)
    agent = models.CharField(max_length=250, db_index=True)

    @staticmethod
    def create_if_not_exist(data):
        try:
            SocketConnection.objects.get(sid=data['sid'])
        except:
            SocketConnection.objects.create( \
                user = data['user'], \
                token = data['token'], \
                sid = data['sid'], \
                agent = data['agent'] \
            )
