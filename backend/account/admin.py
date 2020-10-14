from django.contrib import admin
from account.models import UserProfile
from django.utils.html import mark_safe



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
   
    list_display = [
        'get_main_photo',
        'username', 
        'gender', 
        'is_online', 
        'birthday']