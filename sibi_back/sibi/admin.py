from django.contrib import admin
from .models.ActivosFijos_models import ActivosFijos
from .models.Articulo_models import Articulo
from .models.Cartera_models import Cartera
from .models.CategoriaProducto_models import CategoriaProducto
from .models.Control_models import Control
from .models.IVA_models import IVA
from .models.Marca_models import Marca
from .models.Moneda_models import Moneda
from .models.Proveedor_models import Proveedor
from .models.Referencia_models import Referencia
from .models.Ubicacion_models import Ubicacion



admin.site.register(ActivosFijos)
admin.site.register(Articulo)
admin.site.register(Cartera)
admin.site.register(CategoriaProducto)
admin.site.register(Control)
admin.site.register(IVA)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Referencia)
admin.site.register(Ubicacion)
