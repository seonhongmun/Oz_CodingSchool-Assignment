# Generated by Django 5.1.5 on 2025-01-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed_image',
            field=models.ImageField(blank=True, null=True, upload_to='todo/completed_images'),
        ),
        migrations.AddField(
            model_name='todo',
            name='thumbnail',
            field=models.ImageField(blank=True, default='todo/no_image/NO-IMAGE.gif', null=True, upload_to='todo/thumbnails'),
        ),
    ]
