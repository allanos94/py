# Generated by Django 3.2.8 on 2022-06-19 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220618_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='teamName_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.team'),
        ),
    ]
