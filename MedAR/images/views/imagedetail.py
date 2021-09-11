from rest_framework import generics
from images.serializers import ImageSerializer
from images.models import Image


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for Image detail endpoint"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
