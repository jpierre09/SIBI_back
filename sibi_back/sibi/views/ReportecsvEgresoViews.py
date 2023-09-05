from django.http import HttpResponse, JsonResponse
import csv
from datetime import datetime
from ..models.ActivosFijos_models import ActivosFijos
from django.db.models import Q


'''
Ejemplo de la URL :GET http://127.0.0.1:8000/SIBI/downloadcsv_report_egresos/?fecha_inicio=2023-08-20&fecha_fin=2023-08-20

'''

def download_csv_egresos(request):
    # Recibir las fechas desde la URL
    fecha_inicio_str = request.GET.get('fecha_inicio', None)
    fecha_fin_str = request.GET.get('fecha_fin', None)

    # Si no se proporcionan fechas, devuelve un error
    if not fecha_inicio_str or not fecha_fin_str:
        return JsonResponse({'error': 'Debe proporcionar una fecha de inicio y una fecha de fin'}, status=400)

    # Convertir las fechas en strings a objetos datetime
    fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
    fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()

    # Filtrar la consulta por el rango de fechas y el estado historial es el 1 (ingreso)
    egresos = ActivosFijos.objects.filter(Q(estado_hisorial_id=2) & Q(fecha_ingreso__range=(fecha_inicio, fecha_fin)))
    # print(ingresos)

    # ingresos = ActivosFijos.objects.filter(fecha_ingreso__range=(fecha_inicio, fecha_fin))

    # Si no hay resultados, devolver un mensaje de error
    if not egresos.exists():
        return JsonResponse({'error': 'No hay datos disponibles para el rango de fechas proporcionado'}, status=404)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ingresos.csv"'

    writer = csv.writer(response)
    writer.writerow(['fecha_ingreso', 'proveedor','numero_factura', 'numero_contrato', 'cartera','articulo', 'marca', 'referencia', 'modelo', 'serial', 'vida_util', 'valor_unitario', 'flete', 'placa_amva', 'observaciones', 'created', 'updated'])  # Encabezados del CSV
    
    for egreso in egresos:
        writer.writerow([egreso.fecha_ingreso, egreso.proveedor, egreso.numero_factura, egreso.numero_contrato, egreso.cartera, egreso.articulo, egreso.marca, egreso.referencia, egreso.modelo, egreso.serial, egreso.vida_util, egreso.valor_unitario, egreso.flete, egreso.placa_amva, egreso.observaciones, egreso.created, egreso.updated])

    return response