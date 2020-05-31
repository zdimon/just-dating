from django.contrib import admin

from usermedia.models import UserMedia


@admin.register(UserMedia)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'title', 'user', 'is_main']
