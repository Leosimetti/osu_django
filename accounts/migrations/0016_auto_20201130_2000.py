# Generated by Django 3.1.3 on 2020-11-30 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20201130_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hours_played',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='map_plays',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='successful_map_plays',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='total_score',
        ),
    ]
