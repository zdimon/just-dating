from django.urls import path, include
from chat.views.room import GetRoomView

urlpatterns = [ 
    path('get_room/<int:user_id>',GetRoomView.as_view())
]