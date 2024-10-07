from django import forms
from .models import Contact, Event, Porta, Testimonios

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event 
        fields = ['name', 'description', 'fecha', 'capacidad']    
        
class PortaForm(forms.ModelForm):
    class Meta:
        model = Porta
        fields = ['name_project', 'description', 'url','imagen']

class TestimoniosForm(forms.ModelForm):   
    class Meta:
        model = Testimonios
        fields = ['name','description', 'puesto', 'empresa']                