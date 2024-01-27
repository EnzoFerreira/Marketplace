# Generated by Django 5.0.1 on 2024-01-20 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('weapon_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skin_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to='marketplace/')),
                ('weapon_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='marketplace.weapon_type')),
            ],
        ),
    ]
