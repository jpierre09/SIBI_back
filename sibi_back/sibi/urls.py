from django.urls import path
from .views.ActivosFijosViews import ActivosFijosList, ActivosFijosDetail
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

urlpatterns = [
    # ------- 
    path('ActivosFijos/', ActivosFijosList.as_view(), name='activosfijos-list'),
    path('ActivosFijos/<int:pk>/', ActivosFijosDetail.as_view(), name='activosfijos-detail'),
    # ------- 
    path('articulos/', ArticuloList.as_view(), name='Articulo-list'),
    path('articulos/<int:pk>/', ArticuloDetail.as_view(), name='Articulo-detail'),
    # ------- 
    path('articulos/', CarteraList.as_view(), name='Cartera-list'),
    path('articulos/<int:pk>/', CarteraDetail.as_view(), name='Cartera-detail'),
    # ------- 
    path('articulos/', CategoriaProductoList.as_view(), name='CategoriaProducto-list'),
    path('articulos/<int:pk>/', CategoriaProductoDetail.as_view(), name='CategoriaProducto-detail'),
    # ------- 
    path('articulos/', ConsumiblesList.as_view(), name='Consumibles-list'),
    path('articulos/<int:pk>/', ConsumiblesDetail.as_view(), name='Consumibles-detail'),
    # ------- 
    path('articulos/', ControlList.as_view(), name='Control-list'),
    path('articulos/<int:pk>/', ControlDetail.as_view(), name='Control-detail'),
    # ------- 
    path('articulos/', IVAList.as_view(), name='IVA-list'),
    path('articulos/<int:pk>/', IVADetail.as_view(), name='IVA-detail'),
    # ------- 
    path('articulos/', MarcaList.as_view(), name='Marca-list'),
    path('articulos/<int:pk>/', MarcaDetail.as_view(), name='Marca-detail'),
    # ------- 
    path('articulos/', MonedaList.as_view(), name='Moneda-list'),
    path('articulos/<int:pk>/', MonedaDetail.as_view(), name='Moneda-detail'),
    # ------- 
    path('articulos/', ProveedorList.as_view(), name='Proveedor-list'),
    path('articulos/<int:pk>/', ProveedorDetail.as_view(), name='Proveedor-detail'),
    # ------- 
    path('articulos/', ReferenciaList.as_view(), name='Referencia-list'),
    path('articulos/<int:pk>/', ReferenciaDetail.as_view(), name='Referencia-detail'),
    # ------- 
    path('articulos/', UbicacionList.as_view(), name='Ubicacion-list'),
    path('articulos/<int:pk>/', UbicacionDetail.as_view(), name='Ubicacion-detail'),
    
]