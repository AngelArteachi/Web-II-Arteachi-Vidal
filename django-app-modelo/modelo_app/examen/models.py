from django.db import models

class Localidads(models.Model):
    name = models.CharField(max_length=100, null=False)
    estatus = models.BooleanField(null=False)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=200)
    precio = models.FloatField()
    localidad = models.ForeignKey(Localidads, on_delete=models.CASCADE)
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Evento(models.Model):
    name = models.CharField(max_length=300, null=False)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin = models.DateTimeField(null=False)
    localidad = models.ForeignKey(Localidads, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TipoBoleto(models.Model):
    tipo = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.tipo

class Boleto(models.Model):
    precio = models.FloatField(null=False)
    localidad = models.ForeignKey(Localidads, on_delete=models.CASCADE)
    tipo_boleto = models.ForeignKey(TipoBoleto, on_delete=models.SET_NULL, null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.tipo_boleto} - {self.evento}"

    