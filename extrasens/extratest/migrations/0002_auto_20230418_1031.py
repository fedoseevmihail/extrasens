# Generated by Django 2.2.19 on 2023-04-18 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extratest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrasens_1',
            name='reliability',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='extratest.NumUser'),
        ),
        migrations.AlterField(
            model_name='extrasens_2',
            name='reliability',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='extratest.NumUser'),
        ),
    ]
