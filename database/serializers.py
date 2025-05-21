from rest_framework import serializers
from .models import Experiment

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '_all_'

    def create(self, validated_data):
        # Принудително одобрението е False
        validated_data['approved'] = False
        return super().create(validated_data)
