from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.historial_estado_activos_fijos_models import HistoricoActivosFijos
from ..serializaers.HistorialEstadoAvticosFijosSerializer import HistorialActivosFijos

class CreateHistorial(APIView):
    def post(self, request, format=None):
        serializer = HistorialActivosFijos(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Historial creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUpdateDeleteHistorial(APIView):
    def get(self, request, historial_id, format=None):
        historial = get_object_or_404(HistoricoActivosFijos, pk=historial_id)
        serializer = HistorialActivosFijos(historial)
        return Response(serializer.data)
    
    def put(self, request, historial_id, format=None):
        historial = get_object_or_404(HistoricoActivosFijos, pk=historial_id)
        serializer = HistorialActivosFijos(historial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Historial actualizado exitosamente'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, historial_id, format=None):
        historial = get_object_or_404(HistoricoActivosFijos, pk=historial_id)
        historial.delete()
        return Response({'message': 'Historial eliminado exitosamente'})

class ListHistoriales(APIView):
    def get(self, request, format=None):
        historiales = HistoricoActivosFijos.objects.all()
        serializer = HistorialActivosFijos(historiales, many=True)
        return Response(serializer.data)
    
class ListHistoricosPorActivo(APIView):
    def get(self, request, activo_id, format=None):
        historicos = HistoricoActivosFijos.objects.filter(activo_relacionado=activo_id)
        serializer = HistorialActivosFijos(historicos, many=True)
        return Response(serializer.data)
