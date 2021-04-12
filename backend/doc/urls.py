from django.urls import path, include
from contact.views.contact import ContactListView
from .views import model_graph


urlpatterns = [ 
   
    path('model/',model_graph),
  
]