from django.db import models
from django.core.validators import MaxLengthValidator

# Validacion de errores
from .validation_utils import validate_observaciones

class IVA(models.Model):
    valoriva = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(validators=validate_observaciones(500))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.valoriva)
        