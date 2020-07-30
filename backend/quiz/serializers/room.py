from rest_framework import serializers
from quiz.models import Room, RoomUsers
from account.serializers.profile import UserProfileSerializer

class QuizRoomSerializer(serializers.ModelSerializer):
    
    user_list = serializers.SerializerMethodField()

    def get_user_list(self, obj):
        out = []  
        for u2r in RoomUsers.objects.filter(room=obj):
            out.append(UserProfileSerializer(u2r.user).data)
        return out   


    class Meta:
        model = Room 
        fields = (
            'type',
            'quiz', 
            'question_time', 
            'created_at', 
            'current_question',
            'current_question_text',
            'answers',
            'questions_json',
            'winner',
            'is_done',
            'token',
            'user_list')