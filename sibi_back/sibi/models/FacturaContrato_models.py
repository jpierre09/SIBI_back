from django.db import models
from django.core.validators import MaxLengthValidator

from .Proveedor_models import Proveedor

class FacturaContrato(models.Model):
    numero_factura = models.BigIntegerField(unique=True)
    fecha_factura = models.DateField()
    numero_contrato = models.BigIntegerField(unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Factura: {self.numero_factura}, Contrato: {self.numero_contrato}"
