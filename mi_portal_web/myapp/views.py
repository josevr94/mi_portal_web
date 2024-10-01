from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import ContactForm, EventForm, PortaForm,TestimoniosForm
from .models import Event,Porta,Testimonios

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

def portafolio_lista(request):
    portafolios = Porta.objects.all() 
   
    return render(request,'myapp/portafolio.html',{'portafolio' : portafolios})   

def portafolio_registro(request): 
    if request.method == 'POST':
        form = PortaForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('portafolios')    
    else:
        form = PortaForm()
    return render(request,'myapp/portafolio_registro.html',{'form' : form})   




def registro_testimonio(request):
    if request.method == 'POST':
        form = TestimoniosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonios') 
    else:
        form = TestimoniosForm       
    return render(request,'myapp/registro_testimonios.html',{'form' : form})


    
    
def testimonios_lista(request):
    testimonios = Testimonios.objects.all()
    return render(request,'myapp/testimonios.html', {'testimonios' : testimonios })



def event_register_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request,'myapp/event_register.html',{'form' : form })        
        
def event_list_view(request):
    events = Event.objects.all()  #esto de aca  seria como si hicieramos un SELECT * from events#      
    return render(request, 'myapp/event_list.html',{'events':events})    
# Create your views here.
# aca esta el view el cual es el intermediario entre el template y el modelo, aca va la parte que hara la coneccion 
