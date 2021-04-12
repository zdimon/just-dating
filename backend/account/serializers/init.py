from rest_framework import serializers
from account.serializers.profile import UserProfileSerializer
from contact.serializers.contact import ContactSerializer

class InitSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()
    contacts = serializers.ListField()

    ''' TODO:
        contacts = serializers.ListField( \
            child= ContactSerializer()\
        )
    '''

    # def get_contacts(self, obj):
    #     return obj.user.id

