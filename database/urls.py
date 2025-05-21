from django.urls import path
from .views import ExperimentCreateView, ExperimentDetailView, ExperimentListView, current_user

urlpatterns = [
    path('', ExperimentCreateView.as_view(), name='experiment-create'),
    path('list/', ExperimentListView.as_view(), name='experiment-list'),
    path('<int:id>/', ExperimentDetailView.as_view(), name='experiment-detail'),
    path('api/auth/user/', current_user, name='current-user'),
]