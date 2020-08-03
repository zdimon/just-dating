from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django.core import serializers

from quiz.serializers.message import QuizRoomMessageSerializer, MessageRequestSerializer
from backend.serializers.noauth import NoAuthSerializer
from quiz.models import Room, RoomMessage
from quiz.filters.message import RoomMessageFilter

class GetRoomMessageView(APIView):
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: QuizRoomMessageSerializer, 401: NoAuthSerializer} )

    def get(self, request, token):
        room = Room.objects.filter(token=token)
        messages = RoomMessage.objects.filter(room=room)
        return Response(QuizRoomMessageSerializer(messages, many=True).data)
        

class CreateQuizMessageView(APIView):
    '''
    
    Create a new message in the quiz room.
    '''

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema( 
        request_body=MessageRequestSerializer,
        responses={200: QuizRoomMessageSerializer, 401: NoAuthSerializer} )
    def post(self, request): 
        room = Room.objects.get(token=request.data['room_token'])
        obj = RoomMessage()
        obj.room = room
        obj.user = request.user.userprofile
        obj.text = request.data['message']
        obj.check_answer()
        obj.save()
        return Response(QuizRoomMessageSerializer(obj).data)

