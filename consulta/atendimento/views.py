from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Consulta, Medico, Paciente
from .forms import ConsultaForm
from django.utils import timezone


@login_required
def lista_consultas(request):
    consultas = Consulta.objects.filter(paciente__user=request.user).order_by(
        "data", "horario"
    )
    return render(request, "consultas/lista_consultas.html", {"consultas": consultas})


@login_required
def agendar_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = Paciente.objects.get(user=request.user)
            consulta.save()
            return redirect("lista_consultas")
    else:
        form = ConsultaForm()
    return render(request, "consultas/agendar_consulta.html", {"form": form})


@login_required
def cancelar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id, paciente__user=request.user)
    consulta.status = "Cancelada"
    consulta.save()
    return redirect("lista_consultas")
