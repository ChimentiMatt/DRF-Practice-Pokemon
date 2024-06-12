from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=100)
    evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='species_evolution')
    
    def __str__(self):
        return self.name