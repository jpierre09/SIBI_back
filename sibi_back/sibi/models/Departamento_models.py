from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)