from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from contact.serializers.contact import ContactSerializer
from contact.models import Contact

class ContactListView(generics.ListAPIView):
    '''
    
    Get the contact list of the user.


    '''
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-id')