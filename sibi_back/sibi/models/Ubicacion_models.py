from django.db import models

class Ubicacion(models.Model):
    lugar = models.CharField(max_length=20)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
