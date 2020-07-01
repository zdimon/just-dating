from rest_framework import serializers


class NoAuthSerializer(serializers.Serializer):
    detail = serializers.CharField()
    status_code = serializers.IntegerField()
    status = serializers.IntegerField()
    info = serializers.CharField()