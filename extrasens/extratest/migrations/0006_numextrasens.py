# Generated by Django 2.2.19 on 2023-04-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extratest', '0005_auto_20230414_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumExtrasens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=2, null=True)),
            ],
        ),
    ]