from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)