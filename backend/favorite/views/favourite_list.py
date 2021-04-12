from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from favorite.serializers.favourite import FavouriteSerializer
from favorite.models import Favourite

class FavouriteListView(generics.ListAPIView):
    '''
    
    Get the favourite list of the user.


    '''
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all().order_by('-id')