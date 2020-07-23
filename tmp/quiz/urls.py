# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from .views.index import  new, room_index

urlpatterns = [
    url(r'^new$', new),
    url(r'^$', room_index, name='room_index'),
    
]


### API

from rest_framework import routers
from quiz.views.api.room import *
from quiz.views.api.admin import *

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'theme', ThemeViewSet)

urlpatterns = urlpatterns + [
     url(r'^api/', include(router.urls)),
     url(r'^api/i18n$', i18n),
     url(r'^api/get_active_rooms$', get_active_rooms),
     url(r'^api/admin/save/question$', save_question),
     url(r'^api/admin/delete/question$', delete_question),
     url(r'^api/admin/publish/(?P<id>[^\.]+)/question$', publish_question),
     url(r'^api/admin/unpublish/(?P<id>[^\.]+)/question$', unpublish_question),

     url(r'^api/room/(?P<token>[^\.]+)/info$', room_info),
     url(r'^api/room/(?P<token>[^\.]+)/join$', join_to_room),
     url(r'^api/room/submit$', save_message),
     url(r'^api/room/(?P<token>[^\.]+)/question$', get_question),
     url(r'^api/room/(?P<token>[^\.]+)/users$', get_room_users),
     url(r'^api/room/(?P<token>[^\.]+)/winner$', get_room_winner),
     url(r'^api/room/(?P<room_token>[^\.]+)/next_question$', next_question),
     url(r'^api/room/(?P<room_token>[^\.]+)/user/(?P<user_id>[^\.]+)/detail$', get_user_info),
]

