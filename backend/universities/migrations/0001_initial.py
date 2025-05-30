# Generated by Django 5.2.1 on 2025-05-15 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('website', models.URLField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(default='Monterrey', max_length=100)),
                ('state', models.CharField(default='Nuevo León', max_length=100)),
                ('country', models.CharField(default='Mexico', max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('programs', models.JSONField(blank=True, help_text='JSON field with program details', null=True)),
                ('student_population', models.PositiveIntegerField(blank=True, null=True)),
                ('academic_calendar', models.JSONField(blank=True, help_text='JSON field with academic calendar', null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='university_logos/')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='university_banners/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='TransportationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="E.g., 'Metro Line 1', 'Bus Route 42'", max_length=100)),
                ('transportation_type', models.CharField(choices=[('metro', 'Metro'), ('bus', 'Bus'), ('tram', 'Tram'), ('other', 'Other')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('frequency_minutes', models.PositiveSmallIntegerField(blank=True, help_text='Average frequency in minutes', null=True)),
                ('route_information', models.TextField(blank=True, null=True)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportation_options', to='universities.university')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityPropertyProximity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_meters', models.PositiveIntegerField(help_text='Distance in meters')),
                ('walking_time_minutes', models.PositiveIntegerField(help_text='Estimated walking time in minutes')),
                ('public_transport_time_minutes', models.PositiveIntegerField(blank=True, help_text='Estimated public transport time in minutes', null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_proximities', to='properties.property')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_proximities', to='universities.university')),
            ],
            options={
                'verbose_name': 'University Property Proximity',
                'verbose_name_plural': 'University Property Proximities',
                'unique_together': {('property', 'university')},
            },
        ),
    ]
