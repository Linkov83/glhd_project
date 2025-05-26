from django.urls import path
from .views import ExperimentListCreateView, UserCreateView

urlpatterns = [
    path('', ExperimentListCreateView.as_view(), name='experiment-list-create'),
    path('register/', UserCreateView.as_view(), name='user-register'),
]