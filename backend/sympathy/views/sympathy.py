from rest_framework.views import APIView
from sympathy.models import Sympathy
from account.models import UserProfile
from sympathy.serializers.sympathy import SympathySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from likeuser.models import Like


class SympathyListView(generics.ListAPIView):
    '''
    
    Get the Sympathies list of the user.


    '''
    serializer_class = SympathySerializer
    queryset = Sympathy.objects.all().order_by('-id')