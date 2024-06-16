from django.contrib import admin
from .models.item import Item
from .models.species import Species
from .models.pokemon import Pokemon
from .models.poketype import PokeType

admin.site.register(Item)
admin.site.register(Species)
admin.site.register(Pokemon)
admin.site.register(PokeType)
