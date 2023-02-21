from django.urls import path
from . import views
from django.conf.urls import handler404
from Aplicaciones.qr.views import error_404_view

app_name = "Aplicaciones"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("crear_evento/", views.crear_evento, name="crear_evento"),
    path("autent_qr/", views.autent_qr, name="autent_qr"),
    path("Inscripciones/", views.Inscripciones, name="Inscripciones"),
    path("event_creado/", views.event_creado, name="event_creado"),
   
    path("charts/", views.charts, name="charts"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),

]


