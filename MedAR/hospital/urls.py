from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hospital import views

urlpatterns = [
    path('Doctors/', views.DoctorList.as_view()),
    path('Doctors/<int:pk>/', views.DoctorDetail.as_view()),
    path('Hospital/', views.HospitalList.as_view()),
    path('Hospital/<int:pk>/', views.HospitalDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)



