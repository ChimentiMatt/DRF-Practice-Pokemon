# Generated by Django 4.2.13 on 2024-06-11 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_species_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='species',
            name='evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='species_evolution', to='api.species'),
        ),
    ]
