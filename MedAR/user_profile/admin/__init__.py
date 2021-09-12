from django.contrib import admin
from user_profile.models import Profile
from .user_profile_admin import UserProfileAdmin


admin.site.register(Profile, UserProfileAdmin)