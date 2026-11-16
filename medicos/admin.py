
from django.contrib import admin
from .models import Medico


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos", "especialidad")
    search_fields = ("nombres", "apellidos", "especialidad")
