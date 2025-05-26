from rest_framework import generics, permissions
from .models import Experiment
from .serializers import ExperimentSerializer, UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ExperimentListCreateView(generics.ListCreateAPIView):
    queryset = Experiment.objects.filter(approved=True)
    serializer_class = ExperimentSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(approved=False)  # само одобрени се виждат, новите са approved=False

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]