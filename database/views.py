from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Experiment
from .serializers import ExperimentSerializer

class ExperimentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    lookup_field = 'id'

class ExperimentCreateView(generics.CreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = [IsAuthenticated]

class ExperimentListView(generics.ListAPIView):
    queryset = Experiment.objects.filter(approved=True).order_by("id")
    serializer_class = ExperimentSerializer

@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        return Response({"isAuthenticated": True, "username": request.user.username})
    return Response({"isAuthenticated": False})