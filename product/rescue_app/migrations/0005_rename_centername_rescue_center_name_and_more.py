# Generated by Django 5.1.6 on 2025-02-16 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rescue_app', '0004_rename_centrename_rescue_centername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rescue',
            old_name='centerName',
            new_name='center_name',
        ),
        migrations.RenameField(
            model_name='rescue',
            old_name='form12A',
            new_name='form_12a',
        ),
        migrations.RenameField(
            model_name='rescue',
            old_name='form13A',
            new_name='form_13a',
        ),
        migrations.RenameField(
            model_name='rescue',
            old_name='registrationNumber',
            new_name='registration_number',
        ),
    ]
