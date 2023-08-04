from rest_framework import serializers
from ..models.IVA_models import IVA

class IVASerializer(serializers.ModelSerializer):
    class Meta:
        model = IVA
        fields = '__all__'