from rest_framework import serializers
from ..models.Ubicacion_models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'