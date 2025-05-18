from django.db import models


class Experiment(models.Model):
    Metal_Class = models.CharField(max_length=255, default="From Excel")
    Subclass = models.CharField(max_length=255, default="From Excel")
    Example_Alloy = models.CharField(max_length=255, default="From Excel")
    Chemical_Composition = models.TextField(default="From Excel")
    Laser_Power_W = models.FloatField(default=0.0)
    Scanning_Speed_mm_s = models.FloatField(default=0.0)
    Beam_Spot_Size_and_Profile = models.CharField(max_length=255, default="From Excel")
    Beam_Quality_M2 = models.FloatField(default=0.0)
    Surface_Material = models.CharField(max_length=255, default="From Excel")
    Pre_treatment = models.CharField(max_length=255, default="From Excel")
    Temperature_Range_C = models.IntegerField(default=0)
    Surface_Hardness_HV = models.IntegerField(default=0)
    Hardened_Layer_Depth_mm = models.FloatField(default=0.0)
    Residual_Stresses = models.CharField(max_length=255, default="From Excel")
    Wear_Resistance = models.CharField(max_length=255, default="From Excel")
    Source = models.CharField(max_length=255, default="From Excel")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Example_Alloy} – {self.Laser_Power_W}W"