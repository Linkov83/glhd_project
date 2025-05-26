from rest_framework import serializers
from .models import Experiment
from django.contrib.auth import get_user_model

User = get_user_model()

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 're_password')

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('re_password')
        user = User.objects.create_user(**validated_data, is_active=False)
        return user