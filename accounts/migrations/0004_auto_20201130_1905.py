# Generated by Django 3.1.3 on 2020-11-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hours_played',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='success_rate',
            field=models.FloatField(),
        ),
    ]
