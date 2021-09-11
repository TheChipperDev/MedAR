from rest_framework import generics
from hospital.serializers import DoctorSerializer
from hospital.models import Doctor


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
