import os
import pandas as pd
from django.core.management.base import BaseCommand
from database.models import Experiment

class Command(BaseCommand):
    help = 'Import experiments from Excel file into the database.'

    def handle(self, *args, **kwargs):
        file_path = 'Laser_Hardening_Database.xlsx'  # Ensure this file is in the root dir

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to read Excel file: {e}"))
            return

        # Normalize headers
        df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

        expected_fields = {
            "metal_class", "subclass", "example_alloy", "chemical_composition",
            "laser_power", "scan_speed", "beam_spot", "beam_quality",
            "surface_material", "pre_treatment", "temp_range", "surface_hardness",
            "hardened_layer_depth", "residual_stresses", "wear_resistance", "source"
        }

        missing = expected_fields - set(df.columns)
        if missing:
            self.stdout.write(self.style.ERROR(f"Missing fields in Excel: {missing}"))
            return

        created = 0
        for _, row in df.iterrows():
            try:
                Experiment.objects.create(
                    metal_class=row["metal_class"],
                    subclass=row["subclass"],
                    example_alloy=row["example_alloy"],
                    chemical_composition=row["chemical_composition"],
                    laser_power=row["laser_power"],
                    scan_speed=row["scan_speed"],
                    beam_spot=row["beam_spot"],
                    beam_quality=row["beam_quality"],
                    surface_material=row["surface_material"],
                    pre_treatment=row["pre_treatment"],
                    temp_range=row["temp_range"],
                    surface_hardness=row["surface_hardness"],
                    hardened_layer_depth=row["hardened_layer_depth"],
                    residual_stresses=row["residual_stresses"],
                    wear_resistance=row["wear_resistance"],
                    source=row["source"]
                )
                created += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Skipped row due to error: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Imported {created} experiments successfully."))