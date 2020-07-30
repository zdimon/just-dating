from rest_framework import serializers
from quiz.models import RoomMessage
from account.serializers.profile import UserProfileSerializer



class QuizRoomMessageSerializer(serializers.ModelSerializer):
    
    #owner = serializers.SerializerMethodField()
    #is_readed = serializers.BooleanField(read_only=True)

    # def get_owner(self, obj):
    #     print(obj)
    #     return 222
    #     #return UserProfileSerializer(obj.user).data
       

    class Meta:
        model = RoomMessage
        fields = [
            'id',
            'question',
            'is_right',
            'is_service',
            'room',
            'text',
            'user',
            'created_at',]
# class GetQuizRoomMessageListSerializer(serializers.Serializer):
#     room_id = serializers.IntegerField()
#     messages = QuizRoomMessageSerializer(read_only=True, many=True)