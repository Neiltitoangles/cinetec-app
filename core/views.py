from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail, message
from django.conf import settings

# Vista para la página principal
def index(request):
    return render(request, 'index.html')

# Vista para la página de películas (ESTA ES LA QUE TE DA EL ERROR)
def peliculas(request):
    return render(request, 'peliculas.html')

# Vista para promociones
def promociones(request):
    return render(request, 'promociones.html')

# Vista para dulcería
def dulceria(request):
    return render(request, 'dulceria.html')


def procesar_pago(request):
    if request.method == 'POST':
        # Obtenemos los datos que envía el JavaScript del HTML
        email_cliente = request.POST.get('email')
        total_pago = request.POST.get('total')

        try:
            # Enviamos el correo real
            send_mail(
                'Confirmación de Compra - CINETEC',
                f'¡Hola! Tu pago de S/ {total_pago} ha sido procesado con éxito. ¡Disfruta tu combo!',
                settings.EMAIL_HOST_USER, # Tu correo de adairangles19
                [email_cliente], # El correo que el usuario escribió en la web
                fail_silently=False,
            )
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=400)