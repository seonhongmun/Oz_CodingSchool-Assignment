# Generated by Django 5.1.5 on 2025-01-19 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='is_conpleted',
            new_name='is_completed',
        ),
    ]
