# Generated by Django 5.0.1 on 2024-04-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_weapon_exterior_weapon_float_weapon_skin_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon_inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_count', models.IntegerField()),
                ('weapon_value', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='skin_name',
            new_name='weapon_name',
        ),
    ]
