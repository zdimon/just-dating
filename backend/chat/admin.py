from django.contrib import admin

from chat.models import ChatRoom, ChatRoom2User

class ChatRoom2UserInlineAdmin(admin.TabularInline):
    model = ChatRoom2User

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'token', 'search_key']
    inlines = [ChatRoom2UserInlineAdmin,]
