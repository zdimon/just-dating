from rest_framework import serializers
from contact.models import ContactRequest
from account.serializers.profile import UserProfileSerializer

class ContactRequestSerializer(serializers.ModelSerializer):
    contact_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = ContactRequest
        fields = [
            'contact_user',
            'is_accepted',
            'id'
        ]
