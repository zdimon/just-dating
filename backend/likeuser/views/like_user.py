from rest_framework.views import APIView
from likeuser.models import Like
from account.models import UserProfile
from likeuser.serializers.likes import LikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from sympathy.models import Sympathy
from chat.models import ChatRoom

class LikeCreateView(APIView):
    '''
        Like a User.
        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        liker = request.user.userprofile
        liked = UserProfile.objects.get(pk=user_id)
        try: 
            like = Like.objects.get(liking_user=liker, liked_user=liked)
            print('this user exists')
            return Response({'message':'You have already liked this user'})
        except:
            like = Like()
            like.liking_user = liker
            like.liked_user = liked
            like.save()
            if Like.objects.get(liking_user=liked, liked_user=liker):
                room = ChatRoom.get_or_create(liker,liked)
                Sympathy.objects.create(user1=liked, user2=liker, room=room)
        return Response(LikeSerializer(like).data)