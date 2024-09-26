from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Bienvenido a tu pagina')
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse('Acerca de tu pagina')
    return render(request,'myapp/about.html')

def contact(request):
    # return HttpResponse('Pagina de contacto')
    return render(request,'myapp/contact.html')

def servicios(request):
    # return HttpResponse('Servicios de tu pagina')
    return render(request,'myapp/servicios.html')

def blog(request):
    # return HttpResponse('Blog de la pagina')
    return render(request,'myapp/blog.html')

def our_teams(request):
    return render(request,'myapp/contact.html')

def portafolio(request):
    return render(request,'myapp/contact.html')

def testimonios(request):
    return render(request,'myapp/contact.html')

# Create your views here.
# aca esta el view el cual es el intermediario entre el template y el modelo, aca va la parte que hara la coneccion 
