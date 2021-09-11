from rest_framework import serializers
from hospital.models import Hospital, Doctor

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'location']
