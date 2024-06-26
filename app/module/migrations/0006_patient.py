# Generated by Django 4.0.10 on 2024-06-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_alter_diagnostictest_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('phonenumber', models.IntegerField()),
                ('emailaddress', models.CharField(max_length=150)),
                ('dateofbirth', models.DateField(max_length=8)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
