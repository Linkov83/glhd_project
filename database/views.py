from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Experiment
from .serializers import ExperimentSerializer


# GET, PUT/PATCH, DELETE:
class ExperimentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    lookup_field = 'id'


# POST:
class ExperimentCreateView(generics.CreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


# GET:
class ExperimentListView(generics.ListAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
