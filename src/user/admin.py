from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ["username", 'phone', 'address', 'country', 'additional', ]
    list_display = ["username", 'phone', ]
    list_filter = ["username", 'phone', 'address', 'country', 'additional', ]



admin.site.register(Profile, ProfileAdmin)
