from django.urls import path

from consulta.base.views import home

app_name = "base"
urlpatterns = [
    path("", home, name="home"),
]
