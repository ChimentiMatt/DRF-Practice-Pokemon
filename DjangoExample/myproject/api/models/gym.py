from django.db import models
from accounts.models import Trainer

class Gym(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='trainer')

    def __str__(self):
        return self.name
