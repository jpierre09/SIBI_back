from django.db import models

# Validacion de errores
from .validation_utils import positive_integer_with_max_digits

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    telefono = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    correo = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre)
        