from rest_framework import serializers

from account.serializers.profile import UserProfileSerializer
from favorite.models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    favourite_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Favourite
        fields = [
            'owner',
            'favourite_user',
            'id'
        ]
