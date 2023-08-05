from django.db import models
from .Articulo_models import Articulo
from .Cartera_models import Cartera
from .IVA_models import IVA
from .Marca_models import Marca
from .Moneda_models import Moneda
from .Proveedor_models import Proveedor
from .Referencia_models import Referencia
from .Ubicacion_models import Ubicacion
from .CategoriaProducto_models import CategoriaProducto

from django.core.validators import RegexValidator, MaxValueValidator, MaxLengthValidator, MinValueValidator



class Consumibles(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    numero_factura = models.BigIntegerField(
    validators=[
        MinValueValidator(0), # Asegura que sea un número positivo
        MaxValueValidator(10**50 - 1) # Asegura que no tenga más de 50 dígitos
    ])
    fecha_factura = models.DateField()
    numero_contrato = models.BigIntegerField(
    validators=[
        MinValueValidator(0), # Asegura que sea un número positivo
        MaxValueValidator(10**50 - 1) # Asegura que no tenga más de 50 dígitos
    ])
    cartera = models.ForeignKey(Cartera, on_delete=models.CASCADE)
    categoria_producto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    flete = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.ForeignKey(IVA, on_delete=models.CASCADE)
    observaciones = models.TextField(
        validators=[MaxLengthValidator(500, message='Las observaciones no pueden exceder los 500 caracteres')]
    )
    fotos = models.ImageField(upload_to='consumibles/', null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    numero_convenio = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)