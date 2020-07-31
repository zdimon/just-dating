from django.db import models
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from django.contrib.auth.models import User

from backend.celery import app
from rest_framework.authtoken.models import Token

# channels
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer




class UserProfile(User):
    GENDER = (
        ('male', _('Man')),
        ('female', _('Woman'))
    )

    gender = models.CharField(
        verbose_name=_('Gender'),
        choices=GENDER,
        db_index=True,
        default='male',
        max_length=6)

    publicname = models.CharField(default='', max_length=250)
    is_online = models.BooleanField(default=False)
    account = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    birthday = models.DateField(null=True, blank=True)

    def get_opposite_gender(self):
        if self.gender == 'male':
            return 'female'
        return 'male'

    def get_contacts(self):
        from contact.models import Contact
        return Contact.objects.filter(owner=self)

    def update_online(self):
        from online.models import SocketConnection
        cnt = SocketConnection.objects.filter(user = self).count()
        if cnt == 0:
            self.is_online = False
            self.save()
            self.user_offline_task.delay(self.id)
        else:
            self.is_online = True
            self.save()
            self.user_online_task.delay(self.id)
        

    @app.task
    def user_online_task(user_id):
        from account.serializers.profile import UserProfileSerializer
        payload_user = UserProfile.objects.get(pk=user_id)
        # print('User online task for %s token %s' % (user,token.key))
        channel_layer = get_channel_layer()
        for user in UserProfile.objects.filter(is_online=True, gender=payload_user.get_opposite_gender()):
            token = Token.objects.get(user=user)
            async_to_sync(channel_layer.group_send)( \
                token.key, \
                { \
                    'type': 'user_online', \
                    'message': UserProfileSerializer(payload_user).data \
                }) \

    @app.task
    def user_offline_task(user_id):
        from account.serializers.profile import UserProfileSerializer
        payload_user = UserProfile.objects.get(pk=user_id)
        # print('User online task for %s token %s' % (user,token.key))
        channel_layer = get_channel_layer()
        for user in UserProfile.objects.filter(is_online=True, gender=payload_user.get_opposite_gender()):
            token = Token.objects.get(user=user)
            async_to_sync(channel_layer.group_send)( \
                token.key, \
                { \
                    'type': 'user_offline', \
                    'message': UserProfileSerializer(payload_user).data \
                })