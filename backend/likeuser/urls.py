from django.urls import path, include
from likeuser.views.like_list import LikeListView
from likeuser.views.like_user import LikeCreateView


urlpatterns = [ 
   
    path('list/',LikeListView.as_view()),
    path('add/<int:user_id>/',LikeCreateView.as_view()),
    
]