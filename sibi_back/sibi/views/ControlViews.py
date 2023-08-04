from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.Control_models import Control
from ..serializaers.ControlSerializer import ControlSerializer

class ControlList(APIView):
    def get(self, request):
        activos = Control.objects.all()
        serializer = ControlSerializer(activos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ControlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ControlDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Control, pk=pk)

    def get(self, request, pk):
        activo = self.get_object(pk)
        serializer = ControlSerializer(activo)
        return Response(serializer.data)

    def put(self, request, pk):
        activo = self.get_object(pk)
        serializer = ControlSerializer(activo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activo = self.get_object(pk)
        activo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
