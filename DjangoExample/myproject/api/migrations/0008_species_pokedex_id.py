# Generated by Django 4.2.13 on 2024-06-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_species_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='pokedex_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]