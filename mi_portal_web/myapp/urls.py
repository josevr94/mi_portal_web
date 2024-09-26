from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('servicios/',views.servicios,name='servicios'),
    path("blog/", views.blog, name="blog"),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('testimonios/',views.testimonios, name='testimonios'),
    path('our_teams/', views.our_teams, name='our_teams')
]

# este archivo fue creado por mi, no viene por defecto 
# aca ponemos todos las url de nuestra pagina, si queremos agregar una nueva se tiene q agregar aca 