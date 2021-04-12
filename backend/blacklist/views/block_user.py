from rest_framework.views import APIView
from blacklist.models import BlackList
from account.models import UserProfile
from blacklist.serializers.blacklist import BlackListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class BlackListAddView(APIView):
    '''
        Block User.

        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        sender = request.user.userprofile
        reciver = UserProfile.objects.get(pk=user_id)
        try: 
            bl = BlackList.objects.get(owner=sender, blocked_user=reciver)
            #bl.delete()
            return Response({'message':'This user is already in your black list'})
        except:
            bl = BlackList()
            bl.owner = sender
            bl.blocked_user = reciver
            bl.save()
        return Response(BlackListSerializer(bl).data)