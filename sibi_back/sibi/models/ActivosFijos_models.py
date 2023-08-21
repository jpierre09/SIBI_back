from django.db import models
from .Articulo_models import Articulo
from .Cartera_models import Cartera
from .Control_models import Control
from .IVA_models import IVA
from .Marca_models import Marca
from .Moneda_models import Moneda
from .Proveedor_models import Proveedor
from .Referencia_models import Referencia
from .Ubicacion_models import Ubicacion

# Validacion de errores
from .validation_utils import positive_integer_with_max_digits, validate_observaciones

#Para controlar posibles errores del usuario
from django.core.validators import  MaxValueValidator, MaxLengthValidator


class ActivosFijos(models.Model):
    cantidad = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    numero_factura = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    fecha_ingreso = models.DateField()
    numero_contrato = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    cartera = models.ForeignKey(Cartera, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    vida_util = models.PositiveIntegerField(
        validators=[MaxValueValidator(100, message='La vida útil no puede ser mayor a 100 años')]
    )
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    valor_unitario = models.DecimalField(max_digits=20, decimal_places=10)
    flete = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.ForeignKey(IVA, on_delete=models.CASCADE)
    placa_amva = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    observaciones = models.TextField(validators=validate_observaciones(500))
    foto = models.ImageField(upload_to='activos_fijos/', null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    tipo_activo = models.CharField(max_length=20, default='activo_fijo')

    def __str__(self):
        return str(self.numero_factura)