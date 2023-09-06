from rest_framework import serializers
from .models import ShortUrl


class ShortUrlSerializer(serializers.Serializer):
    url = serializers.CharField()

    def create(self, validated_data):
        return ShortUrl.objects.create(**validated_data)