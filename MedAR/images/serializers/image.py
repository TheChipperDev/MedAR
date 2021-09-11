from rest_framework import serializers
from images.models import Image

class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Image model"""
    class Meta:
        model = Image
        fields = ['id', 'images_directory', 'image_owner']