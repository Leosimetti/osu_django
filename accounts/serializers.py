from rest_framework import serializers
from .models import userProfile, mapPlay


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = userProfile
        fields = '__all__'


class mapPlaySerializer(serializers.ModelSerializer):
    play = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = mapPlay
        fields = '__all__'
