from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from quiz.serializers.message import QuizRoomMessageSerializer
from backend.serializers.noauth import NoAuthSerializer
from quiz.models import Room, RoomMessage
#from chat.filters.message import MessageFilter

class GetRoomMessageView(APIView):
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: QuizRoomMessageSerializer, 401: NoAuthSerializer} )

    def get(self, request, token):
        room = Room.objects.filter(token=token)
        messages = RoomMessage.objects.filter(room=room)
        return Response(QuizRoomMessageSerializer(messages).data)