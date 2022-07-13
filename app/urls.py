from django.urls import path
from .views import home, contact, products, registro,  calcview, SeleccionDie, Rango

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contact, name="contacto"),
    path('productos/', products, name="productos"),
    path('registro/', registro, name="registro"),
    path('calcview/', calcview, name="calcview"),
    path('SeleccionDie/', SeleccionDie, name="SeleccionDie"),
    #path('viewProgress/', viewProgress, name="viewProgress"),
    path('Rango/', Rango, name="Rango"),
    
]