from django.urls import path, include
from contact.views.contact import ContactListView
from contact.views.contact_request \
import ContactRequestCreateView, \
       ContactRequestAcceptView, \
       ContactRequestRefuseView, \
       RequestRejectedListView


urlpatterns = [ 
   
    path('list/',ContactListView.as_view()),
    path('request/rejected/list/',RequestRejectedListView.as_view()),
    path('add/request/<int:user_id>',ContactRequestCreateView.as_view()),
    path('accept/request/<int:request_id>',ContactRequestAcceptView.as_view()),
    path('refuse/request/<int:request_id>',ContactRequestRefuseView.as_view()),
]