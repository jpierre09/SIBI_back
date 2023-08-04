from rest_framework import serializers
from ..models.ActivosFijos_models import ActivosFijos

class ActivosFijosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivosFijos
        fields = '__all__'