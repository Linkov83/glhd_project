from django.db import models

class Experiment(models.Model):
    metal_class = models.CharField(max_length=100)
    subclass = models.CharField(max_length=100)
    example_alloy = models.CharField(max_length=100)
    chemical_composition = models.TextField()
    laser_power_w = models.FloatField()
    scanning_speed_mms = models.FloatField()
    beam_spot_size_and_profile = models.CharField(max_length=100)
    beam_quality_m2 = models.FloatField()
    surface_material = models.CharField(max_length=100)
    pre_treatment = models.CharField(max_length=100)
    temperature_range_c = models.CharField(max_length=50)
    surface_hardness_hv = models.FloatField()
    hardened_layer_depth_mm = models.FloatField()
    residual_stresses = models.CharField(max_length=100)
    wear_resistance = models.CharField(max_length=100)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.example_alloy} – {self.laser_power_w}W @ {self.scanning_speed_mms} mm/s"
