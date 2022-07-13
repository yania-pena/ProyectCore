from django import forms
from .models import Contact, Dietas, IMCalc, tipoDieta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        #fields = ["nombre", "correo","tipo_consulta","mesnaje","avisos"]
        fields = '__all__'
        

        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]
        
## OBTENEMOS LOS DATOS DESDE NUESTRA BASE DE DATOS DIETA
class DietasForm(forms.ModelForm):
     class Meta:
        model = Dietas
        fields = ['user',"nombre","tipoDieta","imagen"]
        
class DietasSelec(forms.ModelForm):
     class Meta:
        model = Dietas
        fields = ["nombre","tipoDieta","imagen"]
        
        
class ImcTotal(forms.ModelForm):
    class Meta:
        model = IMCalc
        fields = '__all__'
        

    
    
    
    
          
# class IMCForm(forms.ModelForm):
    
#     edad = forms.CharField(label='', widget=forms.TextInput(attrs={'rows':2, 'placeholder':'Ingresa tu edad'}), required=True)
#     estatura = forms.CharField(label='', widget=forms.TextInput(attrs={'rows':2, 'placeholder':'Ingresa tu estatura (1,70)'}), required=True)
#     peso = forms.CharField(label='', widget=forms.TextInput(attrs={'rows':2, 'placeholder':'Ingresa tu peso (KG)'}), required=True)

    
    
#     class Meta:
#         model = IMCalc
#         fields = ['genero','edad','estatura','peso']
       
