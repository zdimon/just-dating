from django.contrib import admin

from chat.models import ChatRoom, ChatRoom2User, ChatMessage

class ChatMessageInlineAdmin(admin.TabularInline):
    model = ChatMessage

class ChatRoom2UserInlineAdmin(admin.TabularInline):
    model = ChatRoom2User

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'token', 'search_key', 'has_contact']
    inlines = [ChatRoom2UserInlineAdmin, ChatMessageInlineAdmin]
