from django.contrib import admin
from .models import Event, Porta, Testimonios,Contact,Proyecto, Tarea


admin.site.site_header = "Panel de Administración de MyApp-077"
admin.site.site_title = "MyApp Admin"
admin.site.index_title = "Bienvenido al Administrador de MyApp-077"

class EventAdmin(admin.ModelAdmin):
    list_display= ('name', 'description', 'fecha', 'capacidad')
    search_fields = ('name',)
    
class PortafoliosAdmin(admin.ModelAdmin):
    list_display= ('name_project','description','url', 'imagen')   
    search_fields= ('name_project',) 
    
class TestimoniosAdmin(admin.ModelAdmin):
    list_display= ('name','description','puesto','empresa')
    search_fields= ('name',)
class ContactAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'message')   
    search_fields= ('name',)
    
class ProyectoAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'descripcion', 'fecha_inicio','fecha_fin')   
    search_fields= ('nombre',)    

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha_creacion','completado')
    search_fields = ('nombre',)    
    
admin.site.register(Event, EventAdmin)
admin.site.register(Porta,PortafoliosAdmin)
admin.site.register(Testimonios,TestimoniosAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Tarea,TareaAdmin)
# Register your models here.
