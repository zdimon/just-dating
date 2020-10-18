from rest_framework import serializers

from account.serializers.profile import UserProfileSerializer
from likeuser.models import Like

class LikeSerializer(serializers.ModelSerializer):
    liked_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Like
        fields = [
            'liking_user',
            'liked_user',
            'id'
        ]
