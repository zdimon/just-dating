from rest_framework.views import APIView
from contact.models import ContactRequest, Contact
from account.models import UserProfile
from contact.serializers.contact_request import ContactRequestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class ContactRequestCreateView(APIView):
    '''
        Creating a new request.

        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        sender = request.user.userprofile
        reciver = UserProfile.objects.get(pk=user_id)
        cr = ContactRequest()
        cr.owner = sender
        cr.contact_user = reciver
        cr.save()
        return Response(ContactRequestSerializer(cr).data)

class ContactRequestAcceptView(APIView):
    '''
        Accepting a new request.

        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, request_id):
        cr = ContactRequest.objects.get(pk=request_id)
        cr.is_accepted = True
        cr.is_refused = False
        cr.save()
        Contact.add_contact(cr.owner,cr.contact_user)
        return Response(ContactRequestSerializer(cr).data)

class ContactRequestRefuseView(APIView):
    '''
        Refuse a new request.

        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, request_id):
        cr = ContactRequest.objects.get(pk=request_id)
        cr.is_refused = True
        cr.is_accepted = False
        cr.save()
        return Response(ContactRequestSerializer(cr).data)


class RequestRejectedListView(generics.ListAPIView):
    '''
    
    Get the rejected responces list of the user.


    '''
    serializer_class = ContactRequestSerializer
    queryset = ContactRequest.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = ContactRequest.objects.filter( \
            owner=self.request.user.userprofile, \
            is_refused=True \
        ).order_by('-id')
        return queryset
        