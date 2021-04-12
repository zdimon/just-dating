from rest_framework import serializers

from account.serializers.profile import UserProfileSerializer
from chat.serializers.room import ChatRoomSerializer
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    contact_user = UserProfileSerializer(read_only=True)
    room_token = serializers.SerializerMethodField()


    def get_room_token(self, obj):
        return obj.room.token
      

    class Meta:
        model = Contact
        fields = [
            'room_token',
            'owner',
            'contact_user',
            'id'
        ]
