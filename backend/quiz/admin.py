from django.contrib import admin
from quiz.models import Theme, Question

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
admin.site.register(Theme, ThemeAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'theme', 'get_answers', 'lang', 'level', 'is_published')
    list_filter = ('is_published', 'theme')
    list_editable = ('is_published',)

admin.site.register(Question, QuestionAdmin)