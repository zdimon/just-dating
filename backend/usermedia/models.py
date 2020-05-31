from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import UserProfile

from django.utils.safestring import mark_safe

class UserMedia(models.Model):
    TYPE_MEDIA = (
        ('photo', _('Photo')),
        ('video', _('Video'))
    )

    ORIENTATION = (
        ('land', _('Landscape')),
        ('port', _('Portrait'))
    )

    ROLE_MEDIA = (
        ('public', _('Public')),
        ('private', _('Private'))
    )

    type_media = models.CharField(
        verbose_name=_('Type of media'),
        choices=TYPE_MEDIA,
        default='photo',
        max_length=5)

    role_media = models.CharField(
        verbose_name=_('Role of media'),
        choices=ROLE_MEDIA,
        default='public',
        max_length=10)

    orient = models.CharField(
        verbose_name=_('Orientation'),
        choices=ORIENTATION,
        default='port',
        max_length=5)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    video = models.FileField(blank=True, upload_to='user_video')
    image = models.ImageField(blank=True, upload_to='user_photo')

    @property
    def image_tag(self):
        return mark_safe('<img width="150" src="%s" />' % self.image.url)
