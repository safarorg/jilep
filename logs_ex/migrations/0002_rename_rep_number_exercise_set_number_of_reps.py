# Generated by Django 4.1.6 on 2023-02-12 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs_ex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_set',
            old_name='rep_number',
            new_name='number_of_reps',
        ),
    ]