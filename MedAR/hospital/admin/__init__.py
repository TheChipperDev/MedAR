from django.contrib import admin
from hospital.models import Hospital, Doctor
from .hospital_admin import HospitalAdmin
from .doctor_admin import DoctorAdmin

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Hospital, HospitalAdmin)