# Generated by Django 3.2.8 on 2022-06-17 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220617_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='teamName',
        ),
    ]