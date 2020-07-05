from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from chat.serializers.room import GetRoomRequestSerializer, ChatRoomSerializer
from backend.serializers.noauth import NoAuthSerializer
from chat.models import ChatRoom
from account.models import UserProfile

class GetRoomView(APIView):
    '''
    
    Get or create a new chat room.


    '''

    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: ChatRoomSerializer, 401: NoAuthSerializer} )
    def get(self, request, user_id):
        user_one = request.user.userprofile
        user_two = UserProfile.objects.get(pk=user_id)
        room = ChatRoom.get_or_create(user_one,user_two)
        # print(user_id)
        return Response(ChatRoomSerializer(room,context={'abonent': user_two.id}).data)
