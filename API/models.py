from django.db import models


class Datos(models.Model):
    IDSensor = models.CharField(max_length=20)
    nivelContaminacion = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=3
    )
    latitud = models.DecimalField(default=0.0, decimal_places=6, max_digits=10)
    longitud = models.DecimalField(default=0.0, decimal_places=6, max_digits=10)
    fechaRegistro = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.IDSensor
