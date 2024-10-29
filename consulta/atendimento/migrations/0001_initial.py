import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Medico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_completo", models.CharField(max_length=100)),
                ("especialidade", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_completo", models.CharField(max_length=100)),
                ("data_nascimento", models.DateField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Consulta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.DateField()),
                ("horario", models.TimeField()),
                (
                    "data_agendamento",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pendente", "Pendente"),
                            ("Confirmada", "Confirmada"),
                            ("Cancelada", "Cancelada"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="atendimento.medico",
                    ),
                ),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="atendimento.paciente",
                    ),
                ),
            ],
            options={
                "unique_together": {("medico", "data", "horario")},
            },
        ),
    ]
