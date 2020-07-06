from rest_framework import serializers
from usermedia.models import UserMedia
from account.serializers.profile import UserProfileSerializer

class UserImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMedia
        fields = [
            'id',
            'image',
            'title',
            'is_main',
            'get_small_image_url'
        ]