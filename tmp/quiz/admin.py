# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.models import *
from django.utils.safestring import mark_safe
from django.conf.urls import  url
from quiz.utils import create_test_room 
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class ThemeAdmin(admin.ModelAdmin):
    #pass
    list_display = ('name_ru', 'name_en', 'slug')
admin.site.register(Theme, ThemeAdmin)


class QuestionAdmin(TranslationAdmin):
    #pass
    list_display = ('question', 'theme', 'get_answers', 'lang', 'level', 'is_published')
    list_filter = ('is_published', 'theme')
    list_editable = ('is_published',)
    '''
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    '''

admin.site.register(Question, QuestionAdmin)


class QuizQuestionInline(admin.TabularInline):
    model = Quiz.questions.through
    readonly_fields = ('question',)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'q_count', '_create_room')
    readonly_fields = ('questions',)
    inlines = [QuizQuestionInline]
    fields = ['name']

    def get_urls(self):
         urls = super(QuizAdmin, self).get_urls()
         my_urls = [ url(r'^make_room/(?P<id>\w+)',
                                self.admin_site.admin_view(self.make_room),
                                name="make_room")
                    ]
         return my_urls + urls    

    def make_room(self, request, id):
        q = Quiz.objects.get(pk=id)
        create_test_room(q)
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect('/admin/quiz/room/')

    def _create_room(self,obj):
        return mark_safe(u'<a href="'+reverse('admin:make_room', kwargs={'id': obj.pk})+u'">Создать комнату</a>')  
admin.site.register(Quiz, QuizAdmin)

class RoomQuestionInline(admin.TabularInline):
    model = RoomQuestion
    readonly_fields = ('question', )

class RoomAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'type', 'get_users', 'created_at', 'is_done', '_link_room')
    readonly_fields = ('quiz','current_question', 'token', 'winner', 'answers')
    inlines = [RoomQuestionInline]

    def _link_room(self,obj):
        return mark_safe(u'<a target=_blank href="'+reverse('quiz:room_detail', kwargs={'token': obj.token})+u'">Войти в комнату</a>') 

admin.site.register(Room, RoomAdmin)