from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, IMCalc, tipoDieta , queQuieres, Ejercicios# import models
from .forms import ContactoForm, CustomUserCreationForm, DietasForm, ImcTotal  #, IMCForm# importamos forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
import math
from math import pi
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from django.forms import ValidationError
from app.models import Dietas
from app.models import IMCalc
from django.db.models import Sum, Avg

# Create your views here.
def home(request):
    productos = Producto.objects.all() #hace la consulta y la transforma en una lista
    data = {
        'productos': productos
    }

    return render(request, 'vista\home.html', data)

def contact(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "contacto enviado"
        else:
            data["form"]= formulario

    return render(request, 'vista\contacto.html', data)


def products(request):
    dietas = Dietas.objects.filter(user=request.user)

    data = {
        'dietas': dietas
    }
    current_user = get_object_or_404(User,pk=request.user.pk)

    if request.method == 'POST':
        formD = DietasForm(data=request.POST)

    return render(request, 'vista\productos.html',data)


def SeleccionDie(request, *args, **kwargs):
    #dieta = Dietas.objects.all()
    
    #busca = request.POST.get("dieta2")
   
    die = request.POST.get("buscalo1")
   
  
    if request.method== 'POST':
        que = request.POST.get("buscalo", None)
        if que:
            elige = queQuieres.objects.filter(nombre__contains=que)
            dieta = Dietas.objects.filter(nombre__contains=que)
            if elige:
                print("entraste a elegir")
                datos=[]
                for el in elige:
                    ejerci = el.elige.all()
                    datos.append(dict([(el,ejerci)]))
                print(datos)
                
                return render(request,'imc/agregarimc.html',
                              {'datos':datos})
                    
            else:
                ejercicios = Ejercicios.objects.filter(nombre__contains=que)
                
                return render(request, 'imc/agregarimc.html', {'ejercicios': ejercicios, 'ejercicio':True})
            
    return render(request, 'imc/agregarimc.html')

def registro(request):

    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def calcview(request):
    #date = IMCalc.objects.all().filter(date=datetime.date.today())
    # pes = IMCalc.objects.filter(peso=weight)
    # est = IMCalc.objects.filter(estatura=height)
    # existe = IMCalc.objects.filter(estatura=est).exists()
    data = {}
    if request.method=="POST":
        weight_metric = request.POST.get("weight-metric")
        #weight_imperial = request.POST.get("weight-imperial")

        if weight_metric:

            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric"))

        # elif weight_imperial:
        #     weight = float(request.POST.get("weight-imperial"))/2.205
        #     height = (float(request.POST.get("feet"))*30.48 + float(request.POST.get("inches"))*2.54)/100

        imc = (weight/(height**2))


        save = request.POST.get("save")

        if save == "on":
            IMCalc.objects.create(user=request.user,peso=weight, estatura=height, imc=round(imc))

        if imc < 16:
            state = "ADELGAZAMIENTO EMERGENTE"

        elif imc > 16 and imc < 17:
            state = "ADELGAZAMIENTO MODERADO (Se recomienda dieta subir peso)"
        elif imc > 17 and imc < 18:
            state = "ADELGAZAMIENTO LEVE (Se recomienda dieta subir peso)"
        elif imc > 18 and imc < 25:
            state = "IMC NORMAL"
        elif imc > 25 and imc < 30:
            state = "SOBREPESO"
        elif imc > 30 and imc < 35:
            state = "OBESIDAD TIPO 1"
        elif imc > 35 and imc < 40:
            state = "OBESIDAD TIPO 2"
        elif imc > 40:
            state = "OBESIDAD TIPO 3"

        data["imc"] = imc
        data["state"] = state

    if request.user.is_authenticated:
        dates=[]
        imcs = []
        num = 1

        dates_queryset = IMCalc.objects.all().filter(user=request.user)

        ############333

        for qr in dates_queryset:
            dates.append(str(qr.date)+"("+str(num)+")")
            imcs.append(int(qr.imc))
            num += 1


        plot = figure(x_range=dates, plot_height=500, plot_width=500, title="TUS ESTADISTICAS IMC",
        toolbar_location = "right", tools="")
        plot.title.text_font_size = "20pt"

        plot.xaxis.major_label_text_font_size = "14pt"

        plot.step(dates, imcs, line_width=3)
        plot.legend.label_text_font_size = '14pt'

        plot.xaxis.major_label_orientation = pi/4

        script, div = components(plot)

        data["script"] = script
        data["div"] = div

    return render(request, 'imc/listar.html', data)



def Profile(request):
    current_user = request.user

    return render(request, 'imc/agregarimc.html', data)



# def viewProgress(request):
#     datos = IMCalc.objects.filter(user=request.user)

#     data = {
#         'datos': datos
#     }
    
#     current_user = get_object_or_404(User,pk=request.user.pk)

    
#     return render(request, 'imc\listardietas.html',data)



def Rango(request, *args, **kwargs):
    
    imc = IMCalc.objects.filter(user=request.user) 
    foru = IMCalc.objects.filter(user=request.user).all()
    
    data = {
        'imc': foru
    }
    current_user = get_object_or_404(User,pk=request.user.pk)

    if request.method == 'POST':
        fromd = request.POST.get('from')
        tod = request.POST.get('to')
        
        
       
        search = IMCalc.objects.filter(user=request.user).filter(date__range=[fromd,tod])
        #prom = IMCalc.objects.filter(user=request.user).filter(date__range=[fromd,tod]).aggregate(Sum('peso')/search)
        print(search)
        _avg = IMCalc.objects.filter(user=request.user).filter(date__range=[fromd,tod]).aggregate(avg=Avg(('peso')))
        print(_avg)
        if search and _avg:
            
        
            return render(request,'imc/listardietas.html',
                               {'data': search, "avg": _avg})
       
        else:
        
            return render(request, 'imc/listardietas.html')
        
    return render(request, 'imc/listardietas.html')
    
