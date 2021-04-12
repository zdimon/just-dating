from rest_framework import serializers
from quiz.models import Room
from account.serializers.profile import UserProfileSerializer
from quiz.serializers.question import QuestionSerializer

class QuizRoomSerializer(serializers.ModelSerializer):
    current_question = QuestionSerializer()

    class Meta:
        model = Room 
        fields = (
            'type',
            'created_at', 
            'is_done',
            'current_question',
            'token')
