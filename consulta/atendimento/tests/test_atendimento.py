import pytest
from django.urls import reverse

from consulta.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse("atendimento"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Agendar Consulta</title>")


def test_atendimento_medico(resp, horario):
    assert_contains(resp, horario.medico)
