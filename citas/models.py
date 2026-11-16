
from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico


class Cita(models.Model):

    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("atendida", "Atendida"),
        ("cancelada", "Cancelada"),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.PROTECT
    )

    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length=200)

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default="pendiente"
    )

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico}"
