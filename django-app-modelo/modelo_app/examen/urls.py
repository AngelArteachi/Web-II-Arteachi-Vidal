from django.urls import path

from . import views

urlpatterns = [
    path("index", views.indexExamen, name="index"),
    path('boletos/', views.boletosExamen, name='boletos'),
    path("eventos/", views.eventoExamen, name="evento"),
    path("productos/", views.productosExamen, name="productos")
]