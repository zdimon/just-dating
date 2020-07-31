from django.urls import path, include
from contact.views.contact import ContactListView

urlpatterns = [ 
   
    path('list/',ContactListView.as_view()),
]