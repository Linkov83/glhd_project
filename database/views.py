from rest_framework import generics, permissions
from .models import Experiment
from .serializers import ExperimentSerializer

class ExperimentListView(generics.ListAPIView):
    queryset = Experiment.objects.filter(approved=True).order_by("id")
    serializer_class = ExperimentSerializer

class ExperimentDetailView(generics.RetrieveAPIView):
    queryset = Experiment.objects.filter(approved=True)
    serializer_class = ExperimentSerializer

class ExperimentCreateView(generics.CreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(approved=False)  # Админ ще го одобри после