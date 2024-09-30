from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import ContactForm

def home(request):
    # return HttpResponse('Bienvenido a tu pagina')
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse('Acerca de tu pagina')
    return render(request,'myapp/about.html')

def contact(request):
    # return HttpResponse('Pagina de contacto')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
            
    return render(request,'myapp/contacto.html', {'form': form})

def servicios(request):
    # return HttpResponse('Servicios de tu pagina')
    return render(request,'myapp/servicios.html')

def blog(request):
    # return HttpResponse('Blog de la pagina')
   
    return render(request,'myapp/blog.html')

def our_teams(request):
    teams = [
        {'nombre': 'juan perez', 'puesto' : 'ceo', 'imagen': 'img/ceo.jpg'},
        {'nombre': 'diego prez', 'puesto' : 'junior', 'imagen': 'img/junior.jpg'},
        {'nombre': 'Pedro tanto', 'puesto' : 'senior', 'imagen': 'img/senior.jpg'},
        {'nombre': 'Antai', 'puesto' : 'gerente', 'imagen': 'img/gerente.jpg'},
    ]
    return render(request,'myapp/our_teams.html', {'teams' : teams})

def portafolio(request):
    projects = [
        {'name': 'Pagina de restaurant', 'descripcion' : 'Proyecto para cadena de restaurantes mexicanos','imagen' : 'img/pajaro.jpg', 'url':'https://www.google.com/search?q=restaurant&rlz=1C1CHBF_esCL998CL998&oq=restaurant&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIMCAEQIxgnGIAEGIoFMg0IAhAAGJIDGLEDGIAEMg0IAxAAGJIDGIAEGIoFMg0IBBAAGLEDGMkDGIAEMhMIBRAuGIMBGK8BGMcBGLEDGIAEMhAIBhAuGK8BGMcBGIAEGI4FMgcIBxAAGIAEMhAICBAuGK8BGMcBGIAEGI4FMgcICRAAGIAE0gEIMTM3MWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8'},
        {'name': 'Pagina de Inmobiliarias', 'descripcion' : 'Proyecto para venta de casas','imagen' : 'img/perro.jpg','url':'https://www.google.com/search?q=inmoviliaria&sca_esv=d4fd5f361ef8046d&sca_upv=1&rlz=1C1CHBF_esCL998CL998&sxsrf=ADLYWIIXtivBZke_4SSL1CROW7d4BVXKHQ%3A1727533482752&ei=qhH4ZrbPLdq_5OUPgIaN4AU&ved=0ahUKEwi2zM7c6-WIAxXaH7kGHQBDA1wQ4dUDCA8&uact=5&oq=inmoviliaria&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGlubW92aWxpYXJpYTIKEAAYgAQYkgMYCjILEAAYgAQYkgMYigUyEBAAGIAEGLEDGEMYyQMYigUyDRAuGIAEGNEDGMcBGAoyBxAAGIAEGAoyChAAGIAEGLEDGAoyDRAuGIAEGNEDGMcBGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGApIxyJQAFiJIXAAeAGQAQCYAX2gAaQHqgEEMTEuMbgBA8gBAPgBAZgCDKAC_wfCAgoQIxiABBgnGIoFwgIKEC4YgAQYJxiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIOEAAYgAQYsQMYgwEYigXCAhAQABiABBixAxhDGIMBGIoFwgITEC4YgAQYsQMY0QMYQxjHARiKBcICCBAuGIAEGLEDwgIEECMYJ8ICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICCBAAGIAEGJIDwgILEAAYgAQYsQMYyQPCAggQABiABBixA8ICCxAuGIAEGNEDGMcBwgIFEAAYgATCAhAQLhiABBjRAxhDGMcBGIoFwgIfEC4YgAQY0QMYQxjHARiKBRiXBRjcBBjeBBjgBNgBAZgDALoGBggBEAEYFJIHBDExLjGgB55_&sclient=gws-wiz-serp' },
        {'name': 'Pagina de Escuelas', 'descripcion' : 'Proyecto para escuelas de niños','imagen' : 'img/raton.jpg','url':'https://www.google.com/search?q=escuela&rlz=1C1CHBF_esCL998CL998&oq=escuela&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORixAxjJAxiABDINCAEQABiDARixAxiABDINCAIQABiSAxiABBiKBTINCAMQABiSAxiABBiKBTIMCAQQABhDGIAEGIoFMgYIBRBFGDwyBggGEEUYPDIGCAcQRRg90gEIMTI2MmowajmoAgCwAgA&sourceid=chrome&ie=UTF-8'}
    ]
    return render(request,'myapp/portafolio.html', {'projects': projects})             

def testimonios(request):
    testimonios = [
        {'nombre':'Antai', 'testimonio':'el restaurant fue muy bueno ,buena atencion y la comida esta muy rica ,me gustaria volver'},
        {'nombre':'Violeta', 'testimonio':'el restaurant fue muy bueno ,buena atencion y la comida esta muy rica ,me gustaria volver'},
        {'nombre':'Belen', 'testimonio':'el restaurant fue muy bueno ,buena atencion y la comida esta muy rica ,me gustaria volver'},
        {'nombre':'Jose', 'testimonio':'el restaurant fue muy bueno ,buena atencion y la comida esta muy rica ,me gustaria volver'},
        {'nombre':'Pedro', 'testimonio':''},
        {'nombre':'Juan', 'testimonio':''}
    ]
    return render(request,'myapp/testimonios.html', {'testimonios' : testimonios })

# Create your views here.
# aca esta el view el cual es el intermediario entre el template y el modelo, aca va la parte que hara la coneccion 
