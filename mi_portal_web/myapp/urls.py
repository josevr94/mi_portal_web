from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('servicios/',views.servicios,name='servicios'),
    path("blog/", views.blog, name="blog"),
]
