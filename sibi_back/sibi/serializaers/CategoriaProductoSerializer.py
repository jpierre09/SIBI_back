from rest_framework import serializers
from ..models.CategoriaProducto_models import CategoriaProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'