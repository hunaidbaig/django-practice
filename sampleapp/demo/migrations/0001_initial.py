# Generated by Django 5.0.7 on 2024-07-19 09:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chai/')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('PL', 'PLAIN'), ('GR', 'GINGER'), ('KI', 'KIWI'), ('EL', 'ELAICHI')], max_length=2)),
            ],
        ),
    ]
