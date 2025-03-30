from rest_framework import generics
from .models import Experiment
from .serializers import ExperimentSerializer

# POST: Създаване на експеримент
class ExperimentCreateView(generics.CreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

# GET: Извличане на всички експерименти
class ExperimentListView(generics.ListAPIView):
    queryset = Experiment.objects.all().order_by('-created_at')
    serializer_class = ExperimentSerializer
