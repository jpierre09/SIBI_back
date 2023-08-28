from rest_framework import serializers
from ..models.historial_estado_activos_fijos_models import HistoricoActivosFijos

class HistorialActivosFijos(serializers.ModelSerializer):
    class Meta:
        model = HistoricoActivosFijos
        fields = '__all__'