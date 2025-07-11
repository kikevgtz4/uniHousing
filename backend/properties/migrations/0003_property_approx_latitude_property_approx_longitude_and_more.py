# Generated by Django 5.2.1 on 2025-07-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='approx_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='approx_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='display_area',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='display_neighborhood',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='privacy_radius',
            field=models.IntegerField(default=250),
        ),
    ]
