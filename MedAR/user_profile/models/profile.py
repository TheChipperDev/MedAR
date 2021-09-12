from django.db import models
from django.contrib.auth.models import User
from hospital.models import Hospital, Doctor
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    """Profile model for the Model Table"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_notes = models.TextField(blank=True)
    primary_physician = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    primary_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    adddress = models.CharField(max_length=100, blank=True, default=' ')
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

        
    class Meta:
        """Meta Class for the Profile Model"""
        app_label = 'user_profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()