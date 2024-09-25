"""
URL configuration for mi_portal_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
]
# esta pestaña esta en el archivo principal del django, el cual es el que administra los modulos que iremos creando despues como  el modulo 'myapp'
# en este caso como cremos el modulo myapp. myapp tienen varias url que creamos en ese modulo ,pero para que funcionen tenemos que agregar el modulo completo al archivo principal