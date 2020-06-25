from django.urls import path, include
from account.views.registration import RegistrationView
from account.views.user_list import UserListView
from account.views.login import LoginView

urlpatterns = [ 
    path('registration',RegistrationView.as_view()),
    path('user_list',UserListView.as_view()),
    path('login',LoginView.as_view()),
]