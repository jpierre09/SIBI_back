from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.Proveedor_models import Proveedor
from ..serializaers.ProveedorSerializer import ProveedorSerializer

class ProveedorList(APIView):
    def get(self, request):
        activos = Proveedor.objects.all()
        serializer = ProveedorSerializer(activos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProveedorDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Proveedor, pk=pk)

    def get(self, request, pk):
        activo = self.get_object(pk)
        serializer = ProveedorSerializer(activo)
        return Response(serializer.data)

    def put(self, request, pk):
        activo = self.get_object(pk)
        serializer = ProveedorSerializer(activo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activo = self.get_object(pk)
        activo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
