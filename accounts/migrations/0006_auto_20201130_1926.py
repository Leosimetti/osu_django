# Generated by Django 3.1.3 on 2020-11-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201130_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='successful_map_plays',
            field=models.IntegerField(),
        ),
    ]
