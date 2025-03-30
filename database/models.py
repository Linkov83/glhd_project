from django.db import models

class Experiment(models.Model):
    metal_class = models.CharField(max_length=100)
    subclass = models.CharField(max_length=100)
    example_alloy = models.CharField(max_length=100)
    chemical_composition = models.TextField()
    laser_power = models.FloatField()
    scan_speed = models.FloatField()
    beam_spot = models.CharField(max_length=100)
    beam_quality = models.FloatField()
    surface_material = models.CharField(max_length=100)
    pre_treatment = models.CharField(max_length=100)
    temp_range = models.CharField(max_length=50)
    surface_hardness = models.FloatField()
    hardened_layer_depth = models.FloatField()
    residual_stresses = models.CharField(max_length=100)
    wear_resistance = models.CharField(max_length=100)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.example_alloy} – {self.laser_power}W @ {self.scan_speed}mm/s"
