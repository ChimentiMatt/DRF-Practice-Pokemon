from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Trainer

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name')
    search_fields = ('email',)

admin.site.register(Trainer, MyModelAdmin)
