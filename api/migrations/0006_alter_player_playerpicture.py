# Generated by Django 3.2.8 on 2022-06-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220617_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playerPicture',
            field=models.CharField(max_length=20),
        ),
    ]
