from django.contrib import admin
from .models import Experiment

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ("id", "Example_Alloy", "Laser_Power_W", "approved")
    list_filter = ("approved",)
    search_fields = ("Example_Alloy", "Metal_Class", "Subclass", "Source")
    list_editable = ("approved",)
