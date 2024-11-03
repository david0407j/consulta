import pytest
from django.urls import reverse

from consulta.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse("base:home"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Agendamento de Consultas</title>")


""" def test_email_link(resp):
    assert_contains(resp, 'href="djunio239@gmail.com"') """
