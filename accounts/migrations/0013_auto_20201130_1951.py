# Generated by Django 3.1.3 on 2020-11-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20201130_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hours_played',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='successful_map_plays',
            field=models.IntegerField(default=0),
        ),
    ]