from django.contrib import admin
from account.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username', 
        'gender', 
        'is_online', 
        'birthday']