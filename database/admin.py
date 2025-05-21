from django.contrib import admin
from .models import Experiment

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "Example_Alloy", "Laser_Power_W", "approved"
    )
    list_filter = ("approved", "Metal_Class", "Surface_Material")
    search_fields = ("Example_Alloy", "Source", "Chemical_Composition")
    list_editable = ("approved",)