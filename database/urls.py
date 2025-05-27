from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("🌐 GLHD Backend is running.")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/experiments/", include("database.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),  # за Token login
    path("", index),
]