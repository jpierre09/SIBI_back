from django.db import models
from django.core.validators import MaxLengthValidator


class Control(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(
        validators=[MaxLengthValidator(200, message='La descripción no puede exceder los 200 caracteres')]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)