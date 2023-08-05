from django.db import models
from django.core.validators import MaxLengthValidator


class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(
        validators=[MaxLengthValidator(200, message='La descripción no puede exceder los 200 caracteres')]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre