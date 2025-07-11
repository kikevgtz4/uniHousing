# Generated by Django 5.2.1 on 2025-06-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0006_roommateprofileimage_imagereport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommateprofile',
            name='images_visible_to',
            field=models.CharField(choices=[('everyone', 'Everyone'), ('matches_only', 'Matches Only'), ('connected_only', 'Connected Users Only')], default='everyone', help_text='Who can see your profile images', max_length=20),
        ),
        migrations.AddField(
            model_name='roommateprofile',
            name='profile_visible_to',
            field=models.CharField(choices=[('everyone', 'Everyone'), ('verified_only', 'Verified Users Only'), ('university_only', 'Same University Only')], default='everyone', help_text='Who can see your full profile', max_length=20),
        ),
    ]
