# Generated by Django 5.0.4 on 2024-05-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
