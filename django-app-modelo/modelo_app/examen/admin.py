from django.contrib import admin

from .models import Boleto, Evento, Localidads, Producto, TipoBoleto

admin.site.register(Boleto)
admin.site.register(Evento)
admin.site.register(Localidads)
admin.site.register(Producto)
admin.site.register(TipoBoleto)
