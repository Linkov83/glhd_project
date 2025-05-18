import pandas as pd
from django.core.management.base import BaseCommand
from database.models import Experiment

class Command(BaseCommand):
    help = "Import data from Excel"

    def handle(self, *args, **kwargs):
        try:
            df = pd.read_excel('Laser_Hardening_Database.xlsx')
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Error reading Excel: {e}"))
            return

        success = 0
        for _, row in df.iterrows():
            try:
                Experiment.objects.create(
                    Metal_Class=row['Metal Class'],
                    Subclass=row['Subclass'],
                    Example_Alloy=row['Example Alloy'],
                    Chemical_Composition=row['Chemical Composition'],
                    Laser_Power_W=row['Laser Power (W)'],
                    Scanning_Speed_mm_s=row['Scanning Speed (mm/s)'],
                    Beam_Spot_Size_and_Profile=row['Beam Spot Size and Profile'],
                    Beam_Quality_M2=row['Beam Quality (M²)'],
                    Surface_Material=row['Surface Material'],
                    Pre_treatment=row['Pre-treatment'],
                    Temperature_Range_C=row['Temperature Range (°C)'],
                    Surface_Hardness_HV=row['Surface Hardness (HV)'],
                    Hardened_Layer_Depth_mm=row['Hardened Layer Depth (mm)'],
                    Residual_Stresses=row['Residual Stresses'],
                    Wear_Resistance=row['Wear Resistance'],
                    Source=row['Source'],
                )
                success += 1
            except Exception as e:
                self.stderr.write(self.style.WARNING(f"⚠️ Skipped row due to error: {e}"))

        self.stdout.write(self.style.SUCCESS(f"✅ Imported {success} experiments successfully."))