from django.contrib import admin
from contact.models import Contact, ContactRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['owner', 'contact_user']

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['owner', 'contact_user', 'is_accepted', 'is_refused']

