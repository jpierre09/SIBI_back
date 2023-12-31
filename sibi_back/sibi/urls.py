from django.urls import path

from .views.CombinarActivosConsumiblesViews import ActivosFijosConsumiblesListView
from .views.ActivosFijosViews import ActivosFijosList, ActivosFijosDetail, ActivosFijosEgresadpsList
from .views.ArticuloViews import ArticuloList, ArticuloDetail
from .views.CarteraViews import CarteraList, CarteraDetail
from .views.CategoriaProductoViews import CategoriaProductoList, CategoriaProductoDetail
from .views.ConsumibleViews import ConsumiblesList, ConsumiblesDetail
from .views.ControlViews import ControlList, ControlDetail
from .views.IVAViews import IVAList, IVADetail
from .views.MarcaViews import MarcaList, MarcaDetail
from .views.MonedaViews import MonedaList, MonedaDetail
from .views.ProveedorViews import ProveedorList, ProveedorDetail
from .views.ReferenciaViews import ReferenciaList, ReferenciaDetail
from .views.UbicacionViews import UbicacionList, UbicacionDetail

from .views.PorcentajeDeConsumibles import PorcentajeConsumiblesPorArticuloAPI
from .views.PorcentajeCategoriaConsumible import PorcentajeConsumiblesPorCategoriaAPI

from .views.HistorialEstadoActivosFijosviews import CreateHistorial, GetUpdateDeleteHistorial, ListHistoriales, ListHistoricosPorActivo

from .views.ReportecsvIngresoViews import download_csv
from .views.ReportecsvEgresoViews import download_csv_egresos

urlpatterns = [
    # ------- 
    path('ActivosFijos/', ActivosFijosList.as_view(), name='activosfijos-ingresados'),
    path('ActivosFijos/egresados/', ActivosFijosEgresadpsList.as_view(), name='activosfijos-egresados'),
    path('ActivosFijos/<int:pk>/', ActivosFijosDetail.as_view(), name='activosfijos-detail'),
    # ------- 
    path('articulos/', ArticuloList.as_view(), name='Articulo-list'),
    path('articulos/<int:pk>/', ArticuloDetail.as_view(), name='Articulo-detail'),
    # ------- CreateHistorial
    path('categoriaproductos/', CategoriaProductoList.as_view(), name='CategoriaProducto-list'),
    path('categoriaproductos/<int:pk>/', CategoriaProductoDetail.as_view(), name='CategoriaProducto-detail'),
    
    # ------- Cartera
    path('cartera/', CarteraList.as_view(), name='Cartera-list'),
    path('cartera/<int:pk>/', CarteraDetail.as_view(), name='Cartera-detail'),
    # ------- 
    path('consumible/', ConsumiblesList.as_view(), name='Consumibles-list'),
    path('consumible/<int:pk>/', ConsumiblesDetail.as_view(), name='Consumibles-detail'),
    # ------- 
    path('control/', ControlList.as_view(), name='Control-list'),
    path('control/<int:pk>/', ControlDetail.as_view(), name='Control-detail'),
    # ------- 
    path('iva/', IVAList.as_view(), name='IVA-list'),
    path('iva/<int:pk>/', IVADetail.as_view(), name='IVA-detail'),
    # ------- 
    path('marca/', MarcaList.as_view(), name='Marca-list'),
    path('marca/<int:pk>/', MarcaDetail.as_view(), name='Marca-detail'),
    # ------- 
    path('moneda/', MonedaList.as_view(), name='Moneda-list'),
    path('moneda/<int:pk>/', MonedaDetail.as_view(), name='Moneda-detail'),
    # ------- 
    path('proveedor/', ProveedorList.as_view(), name='Proveedor-list'),
    path('proveedor/<int:pk>/', ProveedorDetail.as_view(), name='Proveedor-detail'),
    # ------- 
    path('referencia/', ReferenciaList.as_view(), name='Referencia-list'),
    path('referencia/<int:pk>/', ReferenciaDetail.as_view(), name='Referencia-detail'),
    # ------- 
    path('ubicacion/', UbicacionList.as_view(), name='Ubicacion-list'),
    path('ubicacion/<int:pk>/', UbicacionDetail.as_view(), name='Ubicacion-detail'),
    
    #----------
    path('listaTotal/', ActivosFijosConsumiblesListView.as_view(), name='Lista_total_activos_fijos_consumibles'),
    path('PorcentajeConsumibleArticulos/', PorcentajeConsumiblesPorArticuloAPI.as_view(), name='porcentaje_consumibles_por_articulo'),
    path('PorcentajeConsumiblesPorCategoria/', PorcentajeConsumiblesPorCategoriaAPI.as_view(), name='Porcentaje_Consumibles_Categoria'),

# Historiales contro de activos fijos

    path('historiales/', ListHistoriales.as_view(), name='historial-list'),
    path('historiales/create/', CreateHistorial.as_view(), name='historial-create'),
    path('historiales/<int:historial_id>/', GetUpdateDeleteHistorial.as_view(), name='historial-detail'),
    # path('historicos_por_activo/<int:activo_id>/', ListHistoricosPorActivo.as_view(), name='historicos-por-activo'),
    path('historicos_por_activo/<str:activo_param>/', ListHistoricosPorActivo.as_view(), name='historicos-por-activo'),
    

    # Descarga reporte en csv ingresos(1) y egresos(2)
    path('downloadcsv_report/', download_csv, name='downloadcsv_repor'),
    path('downloadcsv_report_egresos/', download_csv_egresos, name='downloadcsv_repor_egresos'),

    
]