
from django.db import models


class Paciente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
