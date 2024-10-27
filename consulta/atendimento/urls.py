from django.urls import path
from . import views

urlpatterns = [
    path("consultas/", views.lista_consultas, name="lista_consultas"),
    path("consultas/agendar/", views.agendar_consulta, name="agendar_consulta"),
    path(
        "consultas/cancelar/<int:consulta_id>/",
        views.cancelar_consulta,
        name="cancelar_consulta",
    ),
]
