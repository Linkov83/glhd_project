from django.urls import path
from .views import ExperimentCreateView, ExperimentListView

urlpatterns = [
    path('api/experiments/', ExperimentCreateView.as_view(), name='experiment-create'),
    path('api/experiments/list/', ExperimentListView.as_view(), name='experiment-list'),
]
