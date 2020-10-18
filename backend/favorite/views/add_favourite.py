from rest_framework.views import APIView
from favorite.models import Favourite
from account.models import UserProfile
from favorite.serializers.favourite import FavouriteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class FavouriteCreateView(APIView):
    ''' 
        Adding Favourite.

        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        sender = request.user.userprofile
        reciver = UserProfile.objects.get(pk=user_id)
        try: 
            fav = Favourite.objects.get(owner=sender, favourite_user=reciver)
            fav.delete()
            #return Response({'message':'This user is already in your favourites list'})
        except:
            fav = Favourite()
            fav.owner = sender
            fav.favourite_user = reciver
            fav.save()
        return Response(FavouriteSerializer(fav).data)