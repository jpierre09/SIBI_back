from django.db import models

class Moneda(models.Model):
    tipo = models.CharField(max_length=10)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.tipo