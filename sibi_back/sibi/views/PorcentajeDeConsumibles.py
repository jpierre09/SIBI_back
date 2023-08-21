from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from ..models.Consumibles_models import Consumibles
from ..models.Articulo_models import Articulo

class PorcentajeConsumiblesPorArticuloAPI(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener la suma total de todos los consumibles pero estavuelta los dividi por atiulos
        consumibles_por_articulo = Consumibles.objects.values('articulo').annotate(total_consumibles=Sum('cantidad'))
        
        # aca sumo todos los consumibles
        total_general = Consumibles.objects.aggregate(total=Sum('cantidad'))['total']
        
        # en teoria si no se me olvido calcular poncentaje le saco le porcentaje acad articulo
        porcentaje_por_articulo = []
        for item in consumibles_por_articulo:
            articulo = Articulo.objects.get(pk=item['articulo'])
            porcentaje = (item['total_consumibles'] / total_general) * 100
            porcentaje_por_articulo.append({'articulo': articulo.nombre, 'porcentaje': porcentaje})
        
        return Response({'porcentaje_por_articulo': porcentaje_por_articulo}, status=status.HTTP_200_OK)
