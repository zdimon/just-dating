from django.contrib import admin
from sympathy.models import Sympathy
from chat.models import ChatRoom

@admin.register(Sympathy)
class SympathyAdmin(admin.ModelAdmin):
    list_display = ['user1', 'user2','get_room']
    list_display_links = ['user1', 'user2']
    
    def get_room(self, obj):
        return obj.room.search_key
    get_room.admin_order_field  = 'room'
    get_room.short_description = 'Room'  