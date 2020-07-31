from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from quiz.serializers.room import QuizRoomSerializer
from backend.serializers.noauth import NoAuthSerializer
from quiz.models import Room, Question, Quiz, ROOM_TYPES 
from account.models import UserProfile
import datetime 


class GetRoomView(APIView):
    '''
    
    Get or create a new chat room.


    '''
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: QuizRoomSerializer, 401: NoAuthSerializer} )

    def get(self, request, type, token, lang, lvl, tp, mode, theme):
        question_time = datetime.now()+datetime.timedelta(seconds=60)
        room = Room.get_or_create(type, question_time, lang, lvl, tp, mode, theme, token)
        #room = Room.objects.get(token=token)
        return Response(QuizRoomSerializer(room).data)
