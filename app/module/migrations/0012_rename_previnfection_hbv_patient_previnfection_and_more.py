# Generated by Django 4.0.10 on 2024-06-22 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0011_patient_bloodexposure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='previnfection_hbv',
            new_name='previnfection',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='previnfection_hcv',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='previnfection_hiv',
        ),
    ]
