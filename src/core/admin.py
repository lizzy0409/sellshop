from django.contrib import admin
from .models import Creative_team, Contact, Contact_details

# Register your models here.


class Creative_teamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'image', 'facebook', 'twitter', 'google', 'website', 'mdi_dribbble']
    list_display = ['name', 'image', 'facebook', 'twitter']
    list_filter = ['name', 'image', 'facebook', 'twitter', 'google', 'website', 'mdi_dribbble']


class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'message']
    list_display = ['name', 'email', 'message']
    list_filter = ['name', 'email', 'message']



admin.site.register(Creative_team, Creative_teamAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Contact_details)
