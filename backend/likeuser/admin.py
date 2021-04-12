from django.contrib import admin
from likeuser.models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['liking_user', 'liked_user']
