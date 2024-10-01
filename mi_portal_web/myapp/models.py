from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fecha = models.DateField()
    capacidad = models.IntegerField()
    
class Porta(models.Model):
    name_project = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True,null=True)  
    imagen = models.ImageField(upload_to='img/')  
    
class Testimonios(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()    
    
    
    
    def __str__(self):
        return self.name
