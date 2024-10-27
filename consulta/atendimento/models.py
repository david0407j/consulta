from django.db import models
from django.conf import settings
from django.utils import timezone


class Paciente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome_completo


class Medico(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome_completo} - {self.especialidade}"


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=[
            ("Pendente", "Pendente"),
            ("Confirmada", "Confirmada"),
            ("Cancelada", "Cancelada"),
        ],
    )

    class Meta:
        unique_together = ["medico", "data", "horario"]

    def __str__(self):
        return f"Consulta com {self.medico.nome_completo} para {self.paciente.nome_completo} em {self.data} às {self.horario}"
