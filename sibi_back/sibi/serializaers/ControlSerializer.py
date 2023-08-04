from rest_framework import serializers
from ..models.Control_models import Control

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'