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

    def get_queryset(self):
        try:
            user = self.request.user.userprofile
            if user.gender == 'male':
                return UserProfile.objects.filter(gender='female').order_by('-id')
            else:
                return UserProfile.objects.filter(gender='male').order_by('-id')
        except:
            return UserProfile.objects.filter(gender='female').order_by('-id')

