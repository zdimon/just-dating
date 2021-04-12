from django.urls import path, include
from blacklist.views.blacklist import BlackListView
from blacklist.views.block_user import BlackListAddView


urlpatterns = [ 
   
    path('',BlackListView.as_view()),
    path('add/<int:user_id>/',BlackListAddView.as_view()),
    
]