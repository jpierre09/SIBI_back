from django.db import models

class IVA(models.Model):
    valoriva = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)