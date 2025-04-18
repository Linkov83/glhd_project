# Generated by Django 5.1.6 on 2025-04-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal_class', models.CharField(max_length=100)),
                ('subclass', models.CharField(max_length=100)),
                ('example_alloy', models.CharField(max_length=100)),
                ('chemical_composition', models.TextField()),
                ('laser_power_w', models.FloatField()),
                ('scan_speed_mm_s', models.FloatField()),
                ('beam_diameter_mm', models.FloatField()),
                ('beam_quality_m2', models.CharField(max_length=50)),
                ('laser_type', models.CharField(max_length=100)),
                ('surface_condition', models.CharField(max_length=100)),
                ('shielding_gas', models.CharField(max_length=100)),
                ('defocus_mm', models.FloatField()),
                ('focal_position', models.CharField(max_length=100)),
                ('cooling', models.CharField(max_length=100)),
                ('overlap', models.CharField(max_length=100)),
                ('processing_speed', models.CharField(max_length=100)),
                ('preheating_temp_c', models.FloatField()),
                ('number_of_passes', models.IntegerField()),
                ('energy_density_j_cm2', models.FloatField()),
                ('surface_hardness_hv', models.FloatField()),
                ('hardened_layer_depth_mm', models.FloatField()),
                ('wear_resistance', models.CharField(max_length=100)),
                ('corrosion_resistance', models.CharField(max_length=100)),
                ('residual_stresses', models.CharField(max_length=100)),
                ('microstructure', models.TextField()),
                ('cracks', models.CharField(max_length=100)),
                ('porosity', models.CharField(max_length=100)),
                ('dilution', models.CharField(max_length=100)),
                ('adhesion', models.CharField(max_length=100)),
                ('roughness_ra', models.FloatField()),
                ('remarks', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
