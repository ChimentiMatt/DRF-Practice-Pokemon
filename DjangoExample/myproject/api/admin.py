from django.contrib import admin
from .models.item import Item
from .models.species import Species
from .models.pokemon import Pokemon

admin.site.register(Item)
admin.site.register(Species)
admin.site.register(Pokemon)
