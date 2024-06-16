from django.db import models

class PokeType(models.Model):
    name = models.CharField(max_length=100, default='Normal', null=True)

    def __str__(self):
        return self.name
