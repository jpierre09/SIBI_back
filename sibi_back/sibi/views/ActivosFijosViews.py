from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.ActivosFijos_models import ActivosFijos
from ..serializaers.ActivosFijosSerializer import ActivosFijosSerializer

class ActivosFijosList(APIView):
    def get(self, request):
        activos = ActivosFijos.objects.all()
        serializer = ActivosFijosSerializer(activos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivosFijosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivosFijosDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(ActivosFijos, pk=pk)

    def get(self, request, pk):
        activo = self.get_object(pk)
        serializer = ActivosFijosSerializer(activo)
        return Response(serializer.data)

    def put(self, request, pk):
        activo = self.get_object(pk)
        serializer = ActivosFijosSerializer(activo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activo = self.get_object(pk)
        activo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
