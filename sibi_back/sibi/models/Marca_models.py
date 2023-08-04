from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)