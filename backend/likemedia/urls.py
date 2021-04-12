from django.urls import path, include
from likemedia.views.like_image import LikeCreateView
#from likeuser.views.like_user import LikeCreateView


urlpatterns = [ 
   
    #path('list/',LikeListView.as_view()),
    path('add/<int:image_id>/',LikeCreateView.as_view()),
    
]