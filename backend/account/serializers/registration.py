# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework import serializers
from account.models import UserProfile

class RegistrationRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    birthday = serializers.CharField() # if use DataField we can not define the validator
    gender = serializers.ChoiceField(choices=['male','female'])

    def validate_username(self, value):
        """
        Check that the name is unique.
        """
        error = False
        try:
            UserProfile.objects.get(username=value)
            error = True
        except:
            pass

        if error:
            raise serializers.ValidationError("This username is already exists!!!")
        return value

    def validate_birthday(self, value):
        """
            convert 2020-06-16T21:00:00.000Z -> 2020-06-16
        """
        return value.split('T')[0]


    def save(self):
        profile = UserProfile()
        profile.username = self.validated_data['username']
        profile.password = self.validated_data['password']
        profile.birthday = self.validated_data['birthday']
        profile.gender = self.validated_data['gender']
        profile.save()
        return profile

