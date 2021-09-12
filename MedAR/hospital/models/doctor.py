from django.db import models
from . import Hospital

class Doctor(models.Model):
    """Model for the Doctors Table"""
    name = models.CharField(max_length=100, blank=False, unique=True) # Doctor Name
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE) # Hospitals can have multiple doctors but each doc can only be 1 hosptial


    def __str__(self):
        return self.name
    class Meta:
        """Meta class for Doctor Model"""
        app_label = 'hospital'