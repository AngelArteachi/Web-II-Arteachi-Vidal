from django.urls import path

from . import views

urlpatterns = [
    path("index", views.indexExamen, name="index"),
    path('boletos/', views.boletosExamen, name='boletos'),
    path("boletosCreate/", views.createBoleto, name="boletosCreate"),
    path("eventos/", views.eventoExamen, name="evento"),
    path("eventosCreate/", views.createEvento, name="eventosCreate"),
    path("productos/", views.productosExamen, name="productos")
]