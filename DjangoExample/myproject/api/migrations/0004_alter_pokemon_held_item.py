# Generated by Django 4.2.13 on 2024-06-11 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_item_trainer_alter_pokemon_defense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='held_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='held_item', to='api.item'),
        ),
    ]
