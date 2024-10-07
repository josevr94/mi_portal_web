from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('servicios/',views.servicios,name='servicios'),
    path("blog/", views.blog, name="blog"),
    path('portafolio/registo/', views.portafolio_registro, name='registro_portafolios'),
    path('portafolios/', views.portafolio_lista, name='portafolios'),
    path('testimonios/',views.testimonios_lista, name='testimonios'),
    path('registro/testimonio/', views.registro_testimonio, name='registro_testimonio'),
    path('our_teams/', views.our_teams, name='our_teams'),
    path('events/register/', views.event_register_view, name='event_register'),
    path('events/list/', views.event_list_view, name='event_list'),
    path('proyecto/', views.proyecto, name='proyecto'),
    path('tareas/', views.tarea, name='tareas')
]

# este archivo fue creado por mi, no viene por defecto 
# aca ponemos todos las url de nuestra pagina, si queremos agregar una nueva se tiene q agregar aca 