from rest_framework import serializers

from account.serializers.profile import UserProfileSerializer
from likemedia.models import LikeMedia

class LikeSerializer(serializers.ModelSerializer):
    #liked_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = LikeMedia
        fields = [
            'user',
            'media',
            'id'
        ]
