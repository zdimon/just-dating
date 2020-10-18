from django.contrib import admin
from likemedia.models import LikeMedia
from django.utils.safestring import mark_safe

@admin.register(LikeMedia)
class LikeMediaAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_image','get_user_image']


    def get_user_image(self, obj):
        return obj.media.user
    get_user_image.short_description = 'Image Owner'  

    def get_image(self, obj):
        from usermedia.models import UserMedia
        
        return mark_safe('<img src="%s" />' % obj.media.get_small_image_url) 

        