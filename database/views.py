from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Experiment
from .serializers import ExperimentSerializer


# ✅ Създаване на експеримент (само за логнати потребители)
class ExperimentCreateView(generics.CreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = [IsAuthenticated]


# ✅ Списък само с одобрени експерименти (публично достъпен)
class ExperimentListView(generics.ListAPIView):
    queryset = Experiment.objects.filter(approved=True).order_by("id")
    serializer_class = ExperimentSerializer


# ✅ Детайли на експеримент (публично достъпен)
class ExperimentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    lookup_field = "id"


# ✅ Връща текущия потребител (за frontend логика)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser,
    })