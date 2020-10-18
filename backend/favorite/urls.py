from django.urls import path, include
from favorite.views.favourite_list import FavouriteListView
from favorite.views.add_favourite import FavouriteCreateView


urlpatterns = [ 
   
    path('list/',FavouriteListView.as_view()),
    path('add/<int:user_id>/',FavouriteCreateView.as_view()),
    
]