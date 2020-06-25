# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework import serializers
from account.models import UserProfile
from account.serializers.profile import UserProfileSerializer

class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()


