from django.urls import path, include
from account.views.registration import RegistrationView
urlpatterns = [ 
    path('registration',RegistrationView.as_view()),
]