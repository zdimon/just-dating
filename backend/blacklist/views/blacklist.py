from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from blacklist.serializers.blacklist import BlackListSerializer
from blacklist.models import BlackList

class BlackListView(generics.ListAPIView):
    '''
    
    Get the black list of the user.


    '''
    serializer_class = BlackListSerializer
    queryset = BlackList.objects.all().order_by('-id')