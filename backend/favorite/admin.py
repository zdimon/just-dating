from django.contrib import admin
from favorite.models import Favourite

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['owner', 'favourite_user']
