# Generated by Django 2.2.19 on 2023-04-19 04:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extratest', '0003_auto_20230419_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numuser',
            name='number',
            field=models.CharField(max_length=2, null=True, validators=[django.core.validators.MinValueValidator(1000)], verbose_name='Введите загаданное число'),
        ),
    ]
