from django.http import HttpResponse

def home(request):
    return HttpResponse('Bienvenido a tu pagina')

def about(request):
    return HttpResponse('Acerca de tu pagina')

def contact(request):
    return HttpResponse('Pagina de contacto')

def servicios(request):
    return HttpResponse('Servicios de tu pagina')

def blog(request):
    return HttpResponse('Blog de la pagina')

# Create your views here.
