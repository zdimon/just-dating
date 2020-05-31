from django.urls import path, include
from usermedia.views.add_image import AddImageView


urlpatterns = [ 
    path('add_image',AddImageView.as_view()),
   
]