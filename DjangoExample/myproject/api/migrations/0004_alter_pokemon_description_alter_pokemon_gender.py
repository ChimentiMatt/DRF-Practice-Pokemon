# Generated by Django 4.2.13 on 2024-06-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pokemon_gender_alter_pokemon_trainer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='gender',
            field=models.CharField(default='non-gendered', max_length=15),
        ),
    ]