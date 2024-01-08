# Generated by Django 5.0 on 2024-01-01 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaundryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.laundryservice'),
        ),
    ]
