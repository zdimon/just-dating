from rest_framework import serializers

from account.serializers.profile import UserProfileSerializer
from blacklist.models import BlackList

class BlackListSerializer(serializers.ModelSerializer):
    blocked_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = BlackList
        fields = [
            'owner',
            'blocked_user',
            'id'
        ]
