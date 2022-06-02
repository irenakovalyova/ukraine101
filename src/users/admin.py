from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields=('bio', 'avatar')
    list_display = ['user',]


    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Profile, ProfileAdmin)
