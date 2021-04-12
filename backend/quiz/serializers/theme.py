from rest_framework import serializers
from quiz.models import Theme

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'slug', 'name']
