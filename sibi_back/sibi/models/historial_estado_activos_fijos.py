from django.db import models
from .Dependencia_models import Dependencia
from .RedMonitoreo_models import RedMonitoreo
from .Municipio_models import Municipio
from .ActivosFijos_models import ActivosFijos  
# Validacion de errores
from .validation_utils import positive_integer_with_max_digits, validate_observaciones

class HistorialActivosFijos(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    red_monitoreo = models.ForeignKey(RedMonitoreo, on_delete=models.CASCADE)
    codigo_estacion = models.CharField(max_length=20)
    convenio = models.CharField(max_length=50)
    placa_amva = models.CharField(max_length=20)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    barrio = models.CharField(max_length=100)
    cuenca = models.CharField(max_length=100)
    direccion = models.TextField()
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    activo_relacionado = models.ForeignKey(ActivosFijos, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return f"{self.fecha} - {self.hora} - {self.dependencia} - {self.red_monitoreo} - {self.codigo_estacion} - {self.convenio} - {self.placa_amva} - {self.municipio} - {self.barrio} - {self.cuenca} - {self.direccion} - {self.latitud} - {self.longitud} - {self.descripcion} - {self.is_active} - {self.created} - {self.updated}"
