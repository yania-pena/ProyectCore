from django.contrib import admin
from .models import Dietas, tipoDieta
from .models import MarcaP, Producto, Contact, Profile, IMCalc, Ejercicios, queQuieres
# Register your models here.

class DietasAdmin(admin.ModelAdmin):
    list_display = ["nombre", "tipoDieta", "imagen"]
    list_editable = ["tipoDieta"]
    search_fields = ["nombre"]

class ImcAdmin(admin.ModelAdmin):
    list_display = ["id","user", "imc", "peso", "estatura", "date"]  

admin.site.register(MarcaP)
admin.site.register(Producto)
admin.site.register(tipoDieta)
admin.site.register(Dietas, DietasAdmin)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(IMCalc, ImcAdmin)
admin.site.register(Ejercicios)
admin.site.register(queQuieres)