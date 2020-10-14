from django.urls import path, include
from .index.views import main_page

urlpatterns = [ 
    path('',main_page),
    
]