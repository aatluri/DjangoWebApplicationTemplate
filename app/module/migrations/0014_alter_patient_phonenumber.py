# Generated by Django 4.0.10 on 2024-06-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0013_alter_patient_emailaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phonenumber',
            field=models.CharField(max_length=150),
        ),
    ]
