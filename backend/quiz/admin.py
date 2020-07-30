from django.contrib import admin
from quiz.models import Theme, Question, Room, RoomMessage

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
        'quiz',
        'created_at',
        'question_time',
        'current_question',
        'current_question_text',
        'answers',
        'questions_json',
        'winner',
        'is_done',
        'token',
    )

admin.site.register(Room, RoomAdmin)

class RoomMessageAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'is_right',
        'is_service',
        'room',
        'text',
        'user',
        'created_at',
    )

admin.site.register(RoomMessage, RoomMessageAdmin)
