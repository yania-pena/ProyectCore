from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class tipoDieta(models.Model):
    nombre = models.CharField(max_length=110)
    
    def __str__(self):
        return self.nombre
    
class Dietas(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dietas')
    nombre = models.CharField(max_length=100)
    tipoDieta = models.ForeignKey(tipoDieta, on_delete=models.PROTECT)
    dietaMñn = models.TextField()
    dietaMedmañ = models.TextField()
    dietaTarde = models.TextField()
    dietaMedtar = models.TextField()
    dietaNoche = models.TextField()
    imagen = models.ImageField(upload_to="dietas", null=True)
    
    
    def __str__(self):
        return self.nombre
    
    
class MarcaP(models.Model):
    nombre = models.CharField(max_length=110)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(MarcaP, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="producto", null=True)
    def __str__(self):
        return self.nombre


    
class Ejercicios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='ejercicios')
    #asignar = models.ManyToManyField(queQuieres)
    nombre =  models.CharField(max_length=100)
    tipoEjercicio =  models.CharField(max_length=100)
    Duracion = models.IntegerField()
    Repeticiones = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(300),
            MinValueValidator(1)
        ]
    )
    
    
    
    def __str__(self):
        return f'{self.user.username}: {self.nombre}'

class queQuieres(models. Model):
    nombre = models.CharField(max_length=100)
    elige = models.ManyToManyField(Ejercicios)
    
    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Consulta"],
    [1, "Pedir Asesoramiento"],
    [2, "Felicitaciones"],
    [3, "Reclamo"],
    
    
]


# opciones_PoG = [
#     [0, "Perder Peso"],
#     [1, "Ganar Peso"],
#     [2, "Ganar Musculatura"],
#     [3, "Mantener en Forma"],
    
    
# ]

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    


class IMCalc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imc')
    estatura = models.FloatField()
    peso = models.FloatField()
    imc = models.FloatField()
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user.username}: {self.imc}'



