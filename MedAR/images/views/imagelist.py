from rest_framework import generics

from images.serializers import ImageSerializer
from images.models import Image


class ImageList(generics.ListCreateAPIView):
    """View for ImageList endpoint"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
