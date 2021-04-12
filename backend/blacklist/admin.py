from django.contrib import admin
from blacklist.models import BlackList

@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ['owner', 'blocked_user']
