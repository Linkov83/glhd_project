
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def index(request):
    return HttpResponse("🎉 GLHD Backend is Live!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/experiments/', include('database.urls')),
    path('', index),
]
