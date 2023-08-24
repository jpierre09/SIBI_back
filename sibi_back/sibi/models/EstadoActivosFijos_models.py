from django.db import models
from django.core.validators import MaxLengthValidator


class EstadoActivosFijos(models.Model):
    estado = models.CharField(max_length=100)  # Adjust the max_length according to your needs
    descripcion = models.TextField(validators=[MaxLengthValidator(500)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.estado)
        