# Generated by Django 3.1.3 on 2021-02-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_auto_20210206_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='tag',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
