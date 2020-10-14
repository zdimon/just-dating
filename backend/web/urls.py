from django.urls import path, include
from account.views.registration import RegistrationView
from account.views.user_list import UserListView
from account.views.login import LoginView, LogoutView
from account.views.init import InitView

urlpatterns = [ 
    path('registration',RegistrationView.as_view()),
    
]