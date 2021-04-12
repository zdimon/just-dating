from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import UserProfile

from django.utils.safestring import mark_safe

from backend.settings import BACKEND_URL
from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer


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
    image = ImageCropField(blank=True, upload_to='user_photo')
    cropping = ImageRatioField('image', '80x80')
    #likes = models.IntegerField(default=0)

    @property
    def likes(self):
        from likemedia.models import LikeMedia
        return LikeMedia.objects.filter(media=self).count()

    @property
    def image_tag(self):
        return mark_safe('<img width="150" src="%s" />' % self.image.url)

    @property
    def get_small_image_tag(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_url) 

    @property
    def get_small_image_url(self):
        try:
            return BACKEND_URL+get_thumbnailer(self.image).get_thumbnail({
                'size': (80, 80),
                'box': self.cropping,
                'crop': 'smart',
            }).url 
        except:
            return BACKEND_URL+'noimage.png' 