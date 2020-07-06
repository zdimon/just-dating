# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework import serializers
from chat.models import ChatMessage
from account.serializers.profile import UserProfileSerializer



class ChatRoomMessageSerializer(serializers.ModelSerializer):
    
    owner = serializers.SerializerMethodField()
    is_readed = serializers.BooleanField(read_only=True)

    def get_owner(self, obj):
        return UserProfileSerializer(obj.user).data
       

    class Meta:
        model = ChatMessage
        fields = [
            'id',
            'room',
            'owner',
            'created_at',
            'message',
            'token',
            'is_readed'
        ]

class GetRoomMessageListSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    messages = ChatRoomMessageSerializer(read_only=True, many=True)