from django.db import models


class Medico(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True)

    foto = models.ImageField(
        upload_to="medicos/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
