from django.db import models
from django.core.validators import RegexValidator

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex='^\d+$', message='El NIT debe ser un número entero', code='invalid_number')]
    )
    telefono = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex='^\d+$', message='El teléfono debe ser un número entero', code='invalid_number')]
    )
    correo = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre