from rest_framework import serializers
from account.serializers.profile import UserProfileSerializer

class InitSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()
