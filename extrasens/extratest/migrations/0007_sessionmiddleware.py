# Generated by Django 2.2.19 on 2023-04-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extratest', '0006_usersession'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionMiddleware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
