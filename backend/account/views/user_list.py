from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from account.models import UserProfile
from account.serializers.profile import UserProfileSerializer

class UserListView(generics.ListAPIView):
    '''
    
    List of users.

    ______________
    
    '''
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
