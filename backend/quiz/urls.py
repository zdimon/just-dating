from django.urls import path, include
from quiz.views.theme import ThemeListView, ThemeListViewSet
from quiz.views.room import GetRoomView
from quiz.views.message import GetRoomMessageView, CreateQuizMessageView
urlpatterns = [ 
<<<<<<< HEAD
    path('theme/list',ThemeListView.as_view()),
    path('theme',ThemeListViewSet),
    path('get_room/<str:token>/<str:lang>/<str:type>/<str:lvl>/<str:tp>/<str:mode>/<str:theme>',GetRoomView.as_view()),
=======
    # path('theme/list',ThemeListView.as_view()),
    path('get_room/<str:token>',GetRoomView.as_view()),
>>>>>>> b668b8c072aa290a558879c31c8f966f1ad550ab
    path('get_room_messages/<str:token>', GetRoomMessageView.as_view()),
    path('save_message',CreateQuizMessageView.as_view()),
]