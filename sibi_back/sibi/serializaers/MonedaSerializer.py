from rest_framework import serializers
from ..models.Moneda_models import Moneda

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'