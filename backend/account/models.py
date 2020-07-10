from django.db import models
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
# Create your models here.


from django.contrib.auth.models import User

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


    def update_online(self):
        from online.models import SocketConnection
        cnt = SocketConnection.objects.filter(user = self).count()
        if cnt == 0:
            self.is_online = False
        else:
            self.is_online = True
        self.save()    