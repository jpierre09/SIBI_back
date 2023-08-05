from django.db import models
from django.core.validators import MaxLengthValidator

from .validation_utils import validate_observaciones


# Esta clase aplica unicamente para consumibles
class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(validators=validate_observaciones(500))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.categoria