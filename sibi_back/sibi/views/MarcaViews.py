from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.Marca_models import Marca
from ..serializaers.MarcaSerializer import MarcaSerializer

class MarcaList(APIView):
    def get(self, request):
        activos = Marca.objects.all()
        serializer = MarcaSerializer(activos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarcaDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Marca, pk=pk)

    def get(self, request, pk):
        activo = self.get_object(pk)
        serializer = MarcaSerializer(activo)
        return Response(serializer.data)

    def put(self, request, pk):
        activo = self.get_object(pk)
        serializer = MarcaSerializer(activo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activo = self.get_object(pk)
        activo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
