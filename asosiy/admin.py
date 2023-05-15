from django.contrib import admin

from .models import *
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ( 'nom', 'davlat')
    list_filter = ('davlat',)
    search_fields = ('nom', 'davlat')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ism', 'club')
    list_filter = ('club',)
    search_fields = ('ism',)
    autocomplete_fields = ('club',)

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player', 'eski', 'yangi', 'mavsum', 'narxi')
    list_filter = ('mavsum',)
    search_fields = ('mavsum', 'narxi',)
    autocomplete_fields = ('player','eski', 'yangi')

admin.site.register(Hozirgi_mavsum)

