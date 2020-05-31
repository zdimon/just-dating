from rest_framework import serializers
from account.models import UserProfile
from usermedia.models import UserMedia
from backend.settings import BACKEND_URL

class UserProfileSerializer(serializers.ModelSerializer):

    main_photo = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'username',
            'gender',
            'birthday',
            'main_photo'
        ]
    def get_main_photo(self, obj):
        try:
            media = UserMedia.objects.get(user=obj, is_main=True, type_media='photo')
            return BACKEND_URL+media.image.url
        except:
            return 'no image'