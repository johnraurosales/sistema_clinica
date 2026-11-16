
from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos", "dni", "telefono")
    search_fields = ("nombres", "apellidos", "dni")
