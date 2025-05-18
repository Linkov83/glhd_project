from django.db import models

class Experiment(models.Model):
    Metal_Class = models.CharField(max_length=100)
    Subclass = models.CharField(max_length=100)
    Example_Alloy = models.CharField(max_length=100)
    Chemical_Composition = models.TextField()
    Laser_Power_W = models.FloatField()
    Scanning_Speed_mm_s = models.FloatField()
    Beam_Spot_Size_and_Profile = models.CharField(max_length=100)
    Beam_Quality_M2 = models.CharField(max_length=100)
    Surface_Material = models.CharField(max_length=100)
    Pre_Treatment = models.CharField(max_length=100)
    Temperature_Range_C = models.CharField(max_length=50)
    Surface_Hardness_HV = models.FloatField()
    Hardened_Layer_Depth_mm = models.FloatField()
    Residual_Stresses = models.CharField(max_length=100)
    Wear_Resistance = models.CharField(max_length=100)
    Source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Example_Alloy} – {self.Laser_Power_W}W @ {self.Scanning_Speed_mm_s}mm/s