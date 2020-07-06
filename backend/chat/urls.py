from django.urls import path, include
from chat.views.room import GetRoomView
from chat.views.message import GetRoomMessageView, CreateRoomMessageView

urlpatterns = [ 
    path('get_room/<int:user_id>',GetRoomView.as_view()),
    path('get_room_messages',GetRoomMessageView.as_view()),
    path('create_message/',CreateRoomMessageView.as_view()),
]