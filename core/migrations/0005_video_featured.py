# Generated by Django 5.0.4 on 2024-05-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_video_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]