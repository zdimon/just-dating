from django.contrib import admin
from quiz.models import Theme, Question, Room, RoomMessage, RoomQuestion, Smile, Sticker

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
admin.site.register(Theme, ThemeAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'theme', 'get_answers', 'lang', 'level', 'is_published')
    list_filter = ('is_published', 'theme')
    list_editable = ('is_published',)

admin.site.register(Question, QuestionAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'created_at',
        'is_done',
        'token',
        'current_question'
    )

admin.site.register(Room, RoomAdmin)

class RoomMessageAdmin(admin.ModelAdmin):
    list_display = (
        'is_right',
        'is_service',
        'room',
        'text',
        'user',
        'created_at',
    )

admin.site.register(RoomMessage, RoomMessageAdmin)


class RoomQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'room',
        'is_done'
    )

admin.site.register(RoomQuestion, RoomQuestionAdmin)


class SmileAdmin(admin.ModelAdmin):
    list_display = (
        'smile',
    )

admin.site.register(Smile, SmileAdmin)


class StickerAdmin(admin.ModelAdmin):
    list_display = (
        'sticker',
    )

admin.site.register(Sticker, StickerAdmin)
