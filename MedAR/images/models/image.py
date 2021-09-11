from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    """Image Model for the Image table"""
    images_directory = models.CharField(max_length=250, blank=False)
    image_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        """Meta class for Image model"""
        app_label = 'images'