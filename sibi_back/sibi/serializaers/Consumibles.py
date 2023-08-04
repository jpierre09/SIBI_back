from rest_framework import serializers
from ..models.Consumibles_models  import Consumibles

class ConsumiblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumibles
        fields = '__all__'