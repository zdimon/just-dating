from django.urls import path, include
from quiz.views.theme import ThemeListView, ThemeListViewSet
from quiz.views.room import GetRoomView
from quiz.views.message import GetRoomMessageView
urlpatterns = [ 
    path('theme/list',ThemeListView.as_view()),
    path('theme',ThemeListViewSet),
    path('get_room/<str:token>',GetRoomView.as_view()),
    path('get_room_messages/<str:token>', GetRoomMessageView.as_view()),
]