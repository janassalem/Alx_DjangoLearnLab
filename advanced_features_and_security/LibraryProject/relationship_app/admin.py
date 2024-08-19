from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

admin.site.register(UserProfile, UserProfileAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)