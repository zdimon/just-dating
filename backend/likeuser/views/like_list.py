from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from likeuser.serializers.likes import LikeSerializer
from likeuser.models import Like

class LikeListView(generics.ListAPIView):
    '''
    
    Get the list of users that a user is likes.


    '''
    serializer_class = LikeSerializer
    queryset = Like.objects.all().order_by('-id')