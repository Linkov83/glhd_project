# database/serializers.py
from rest_framework import serializers
from .models import Experiment

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = "__all__"
        read_only_fields = ['approved']
