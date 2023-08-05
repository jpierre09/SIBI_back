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

#Para controlar posibles errores del usuario
from django.core.validators import RegexValidator, MaxValueValidator, MaxLengthValidator, MinValueValidator


class ActivosFijos(models.Model):
    cantidad = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    numero_factura = models.BigIntegerField(
    validators=[
        MinValueValidator(0), # Asegura que sea un número positivo
        MaxValueValidator(10**50 - 1) # Asegura que no tenga más de 50 dígitos
    ])
    fecha_ingreso = models.DateField()
    numero_contrato = models.BigIntegerField(
    validators=[
        MinValueValidator(0), # Asegura que sea un número positivo
        MaxValueValidator(10**50 - 1) # Asegura que no tenga más de 50 dígitos
    ])
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
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    flete = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.ForeignKey(IVA, on_delete=models.CASCADE)
    placa_amva = models.BigIntegerField(
    validators=[
        MinValueValidator(0), # Asegura que sea un número positivo
        MaxValueValidator(10**50 - 1) # Asegura que no tenga más de 50 dígitos
    ])
    observaciones = models.TextField(
        validators=[MaxLengthValidator(500, message='Las observaciones no pueden exceder los 500 caracteres')]
    )
    foto = models.ImageField(upload_to='activos_fijos/', null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)