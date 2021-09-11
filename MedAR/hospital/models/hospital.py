from django.db import models


class Hospital(models.Model):
    """Model for the Hospital table"""
    name = models.CharField(max_length=100, blank=False, unique=True)
    location = models.CharField(max_length=100, blank=True, default=' ') # location of the hospital

    class Meta:
        app_label = 'hospital'
        