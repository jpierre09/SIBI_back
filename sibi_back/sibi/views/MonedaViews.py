from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.Moneda_models import Moneda
from ..serializaers.MonedaSerializer import MonedaSerializer

class MonedaList(APIView):
    def get(self, request):
        activos = Moneda.objects.all()
        serializer = MonedaSerializer(activos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MonedaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MonedaDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Moneda, pk=pk)

    def get(self, request, pk):
        activo = self.get_object(pk)
        serializer = MonedaSerializer(activo)
        return Response(serializer.data)

    def put(self, request, pk):
        activo = self.get_object(pk)
        serializer = MonedaSerializer(activo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activo = self.get_object(pk)
        activo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
