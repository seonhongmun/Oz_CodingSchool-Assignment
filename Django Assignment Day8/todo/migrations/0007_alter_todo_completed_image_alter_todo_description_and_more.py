# Generated by Django 5.1.5 on 2025-02-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_todo_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_image',
            field=models.ImageField(blank=True, null=True, upload_to='todo/completed_images', verbose_name='썸네일 이미지'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateField(verbose_name='종료일'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='완료여부'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateField(verbose_name='시작일'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50, verbose_name='제목'),
        ),
    ]
