from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Value, CharField
from ..models.ActivosFijos_models import ActivosFijos
from ..models.Consumibles_models import Consumibles
from ..serializaers.ActivosFijosSerializer import ActivosFijosSerializer
from ..serializaers.ConsumiblesSerializer import ConsumiblesSerializer

class ActivosFijosConsumiblesListView(APIView):
    def get(self, request, *args, **kwargs):
        activos_fijos = ActivosFijos.objects.annotate(tipo_activo=Value('activo_fijo', output_field=CharField()))
        consumibles = Consumibles.objects.annotate(tipo_activo=Value('consumible', output_field=CharField()))

        combined_queryset = list(activos_fijos) + list(consumibles)
        serializer_class = ActivosFijosSerializer if any(item.tipo_activo == 'activo_fijo' for item in combined_queryset) else ConsumiblesSerializer

        serializer = serializer_class(combined_queryset, many=True)
        return Response(serializer.data)
