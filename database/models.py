from django.db import models

class Experiment(models.Model):
    Example_Alloy = models.CharField(max_length=255)
    Laser_Power_W = models.FloatField()
    Scanning_Speed_mm_s = models.FloatField()
    Beam_Spot_Size_and_Profile = models.CharField(max_length=255)
    Beam_Quality_M2 = models.CharField(max_length=255)
    Surface_Material = models.CharField(max_length=255)
    Pre_treatment = models.CharField(max_length=255)
    Temperature_Range_C = models.CharField(max_length=255)
    Surface_Hardness_HV = models.FloatField()
    Hardened_Layer_Depth_mm = models.FloatField()
    Residual_Stresses = models.CharField(max_length=255)
    Wear_Resistance = models.CharField(max_length=255)
    Metal_Class = models.CharField(max_length=255)
    Subclass = models.CharField(max_length=255)
    Chemical_Composition = models.TextField()
    Source = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Example_Alloy} – {self.Laser_Power_W}W @ {self.Scanning_Speed_mm_s}mm/s"