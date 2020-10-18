from rest_framework import serializers

from account.serializers.profile import UserProfileSerializer
from sympathy.models import Sympathy

class SympathySerializer(serializers.ModelSerializer):
    #user2 = UserProfileSerializer(read_only=True)

    class Meta:
        model = Sympathy
        fields = [
            'user1',
            'user2',
            'room',
            'id'
        ]
