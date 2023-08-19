from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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
from .models.Consumibles_models  import Consumibles
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin

class CustomGroupAdmin(GroupAdmin):
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Permisos', {'fields': ('permissions',)}),
        
    )
    search_fields = ('name',)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

class MyAdminSite(AdminSite):
    site_title = 'Sistema Integral de Bienes y Servicios'
    site_header = 'Administrador de SIBI'
    index_title = 'Que ponemos en este lado????'
    def each_context(self, request):
        context = super().each_context(request)
        context['site_url'] = 'https://geoportal.siata.gov.co/geoportal/'  # jajaja se puede mandar ver sitio a cualquier lado 
        return context

admin_site = MyAdminSite(name='SIBI')


#admin por defecto
# admin.site.register(ActivosFijos)
# admin.site.register(Articulo)
# admin.site.register(Cartera)
# admin.site.register(CategoriaProducto)
# admin.site.register(Control)
# admin.site.register(IVA)
# admin.site.register(Marca)
# admin.site.register(Proveedor)
# admin.site.register(Referencia)
# admin.site.register(Ubicacion)
# admin.site.register(Moneda)
# admin.site.register(Consumibles)

#admin personalizado

admin_site.register(ActivosFijos)
admin_site.register(Articulo)
admin_site.register(Cartera)
admin_site.register(CategoriaProducto)
admin_site.register(Control)
admin_site.register(IVA)
admin_site.register(Marca)
admin_site.register(Proveedor)
admin_site.register(Referencia)
admin_site.register(Ubicacion)
admin_site.register(Moneda)
admin_site.register(Consumibles)

admin_site.register(Group,CustomGroupAdmin)
admin_site.register(Permission)
admin_site.register(User,CustomUserAdmin)