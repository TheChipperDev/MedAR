from rest_framework import generics
from hospital.serializers import DoctorSerializer
from hospital.models import Doctor


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
