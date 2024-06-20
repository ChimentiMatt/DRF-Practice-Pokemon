from django.db import models
from .item import Item
from .species import Species
from accounts.models import Trainer
from .poketype import PokeType

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    experience_points = models.IntegerField(default=0)
    description = models.TextField(default='')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True, related_name='pokemon_items')
    gender = models.CharField(max_length=15, default='non-gendered')
    happiness = models.IntegerField(default=1)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='species', null=True, blank=True)
    pokedex_id = models.IntegerField(unique=True, null=True, blank=True)
    # image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    hit_points = models.IntegerField(default=1)
    attack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    special_attack = models.IntegerField(default=1)
    special_defense = models.IntegerField(default=1)
    speed = models.IntegerField(default=1)

    poke_type =  models.ForeignKey(PokeType, on_delete=models.CASCADE, related_name='poke_type', null=True, blank=True)
    # abilities = models.ForeignKey(Abilites, on_delete=models.CASCADE, related_name='abilities')
    # moves = models.ForeignKey(Moves, on_delete=models.CASCADE, related_name='moves')
    held_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True, related_name='held_item')

    def __str__(self):
        return self.name
