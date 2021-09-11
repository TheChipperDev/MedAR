from rest_framework import generics
from hospital.serializers import HospitalSerializer
from hospital.models import Hospital


class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
