# Generated by Django 5.0.2 on 2024-02-08 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_session_year_id_student_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='start',
            new_name='session_year_id',
        ),
    ]
