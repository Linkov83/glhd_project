import pandas as pd
from django.core.management.base import BaseCommand
from database.models import Experiment

class Command(BaseCommand):
    help = 'Импортира експерименти от Excel файл'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='Път до Excel файла')

    def handle(self, *args, **kwargs):
        filepath = kwargs['filepath']
        df = pd.read_excel(filepath)

        for _, row in df.iterrows():
            Experiment.objects.create(
                metal_class=row['Metal Class'],
                subclass=row['Subclass'],
                example_alloy=row['Example Alloy'],
                chemical_composition=row['Chemical Composition'],
                laser_power=row['Laser Power (W)'],
                scan_speed=row['Scan Speed (mm/s)'],
                beam_spot=row['Beam Spot'],
                beam_quality=row['Beam Quality'],
                surface_material=row['Surface Material'],
                pre_treatment=row['Pre-treatment'],
                temp_range=row['Temp Range'],
                surface_hardness=row['Hardness (HV)'],
                hardened_layer_depth=row['Layer Depth (mm)'],
                residual_stresses=row['Residual Stresses'],
                wear_resistance=row['Wear Resistance'],
                source=row['Source'],
            )

        self.stdout.write(self.style.SUCCESS('✅ Успешен импорт на експерименти!'))
