# Generated by Django 2.2.19 on 2023-04-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extratest', '0008_auto_20230420_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='session_key',
            field=models.CharField(default='', max_length=40),
        ),
    ]
