from django.urls import path
from .views import ExperimentCreateView, ExperimentListView

urlpatterns = [
    path('', ExperimentCreateView.as_view(), name='experiment-create'),  # /api/experiments/
    path('list/', ExperimentListView.as_view(), name='experiment-list'),  # /api/experiments/list/
]
