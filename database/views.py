from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Experiment
from .serializers import ExperimentSerializer


# GET, PUT/PATCH, DELETE: Работа с единичен експеримент
class ExperimentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    lookup_field = 'id'  # Позволява достъп чрез /<id>/ вместо /<pk>/


# POST: Създаване на експеримент
class ExperimentCreateView(generics.CreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


# GET: Извличане на всички експерименти
class ExperimentListView(generics.ListAPIView):
    queryset = Experiment.objects.all().order_by('-created_at')
    serializer_class = ExperimentSerializer
