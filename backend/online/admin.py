from django.contrib import admin

from online.models import SocketConnection

@admin.register(SocketConnection)
class SocketConnectionAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'sid',
        'token', 
        'agent'
        ]
