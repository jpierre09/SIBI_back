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

# Validacion de errores
from .validation_utils import positive_integer_with_max_digits, validate_observaciones


class Consumibles(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    numero_factura = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    fecha_factura = models.DateField()
    numero_contrato = models.BigIntegerField(validators=positive_integer_with_max_digits(50))
    cartera = models.ForeignKey(Cartera, on_delete=models.CASCADE)
    categoria_producto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    flete = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.ForeignKey(IVA, on_delete=models.CASCADE)
    observaciones = models.TextField(validators=validate_observaciones(500))
    fotos = models.ImageField(upload_to='consumibles/', null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    numero_convenio = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tipo_activo = models.CharField(max_length=20, default='consumible',editable=False)

    def __str__(self):
        return str(self.articulo)