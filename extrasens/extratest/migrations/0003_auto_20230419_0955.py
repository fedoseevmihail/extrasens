# Generated by Django 2.2.19 on 2023-04-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extratest', '0002_auto_20230418_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrasens_1',
            name='reliability',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='extrasens_2',
            name='reliability',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
