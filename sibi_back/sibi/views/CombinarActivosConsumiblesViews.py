from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Value, CharField
from ..models.ActivosFijos_models import ActivosFijos
from ..models.Consumibles_models import Consumibles
from ..serializaers.ActivosFijosSerializer import ActivosFijosSerializer
from ..serializaers.ConsumiblesSerializer import ConsumiblesSerializer


class ActivosFijosConsumiblesListView(APIView):
    def get(self, request, *args, **kwargs):
        activos_fijos = ActivosFijos.objects.all()
        consumibles = Consumibles.objects.all()

        activos_serialized = ActivosFijosSerializer(activos_fijos, many=True).data
        consumibles_serialized = ConsumiblesSerializer(consumibles, many=True).data

        combined_data = activos_serialized + consumibles_serialized

        return Response(combined_data)


