# Generated by Django 4.2.13 on 2024-06-23 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_pokadex_id_pokemon_pokedex_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
