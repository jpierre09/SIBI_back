from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from ..models.Consumibles_models import Consumibles
from ..models.CategoriaProducto_models import CategoriaProducto

class PorcentajeConsumiblesPorCategoriaAPI(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener la suma total de todos los consumibles pero estavuelta los dividi por atiulos
        consumibles_por_categoria = Consumibles.objects.values('categoria_producto').annotate(total_consumibles=Sum('cantidad'))
        
        print(consumibles_por_categoria)
        
        # aca sumo todos los consumibles
        total_general = Consumibles.objects.aggregate(total=Sum('cantidad'))['total']
        
        # en teoria si no se me olvido calcular poncentaje le saco le porcentaje acad articulo
        porcentaje_por_categoria = []
        for item in consumibles_por_categoria:
            categoria = CategoriaProducto.objects.get(pk=item['categoria_producto'])
            porcentaje = (item['total_consumibles'] / total_general) * 100
            porcentaje_por_categoria.append({'categoria': categoria.categoria, 'porcentaje': porcentaje})
        
        return Response({'porcentaje_por_categoria': porcentaje_por_categoria}, status=status.HTTP_200_OK)
