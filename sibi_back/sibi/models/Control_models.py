from django.db import models


class Control(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)