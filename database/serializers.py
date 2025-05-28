from rest_framework import serializers
from .models import Experiment
from django.contrib.auth import get_user_model
import re

User = get_user_model()

def to_snake_case(text):
    # Заменя интервали, скоби, запетаи и други с "_"
    text = re.sub(r'\W+', '_', text)
    return text.lower()

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {to_snake_case(key): value for key, value in data.items()}

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
        try:
            user = User.objects.create_user(**validated_data, is_active=False)
        except Exception as e:
            print("ERROR:", e)
            raise e
        return user
