from django.urls import path, include
from sympathy.views.sympathy import SympathyListView


urlpatterns = [ 
   
    #path('',SympathyCreateView.as_view()),
    path('list/',SympathyListView.as_view()),
    
    
]