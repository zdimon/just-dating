from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from chat.serializers.message import GetRoomMessageListSerializer, ChatRoomMessageSerializer
from backend.serializers.noauth import NoAuthSerializer
from chat.models import ChatRoom, ChatMessage
from chat.filters.message import MessageFilter

class GetRoomMessageView(generics.ListAPIView):
    '''
    
    Get room messages.


    '''
    serializer_class = ChatRoomMessageSerializer
    filterset_class = MessageFilter
    queryset = ChatMessage.objects.all().order_by('-id')

class CreateRoomMessageView(generics.CreateAPIView):
    '''
    
    Create a new message in the room.


    '''
    queryset = ChatMessage.objects.all()
    serializer_class = ChatRoomMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        room = ChatRoom.objects.get(token=serializer.validated_data['token'])
        serializer.save(user=self.request.user.userprofile, room=room)