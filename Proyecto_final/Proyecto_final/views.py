from django.http import HttpResponse
from django.views import View
from django.shortcuts import render 
import json

def portafolio(request):

    return HttpResponse("Proyecto Final")

class VistaDatos(View):
    template_name ="portafolio.html"

    def post(self,request):
        return render(request)
    
    def get(self,request):
        nombre = "Mario Aceves"
        edad = 30
        sexo = "Masculino"
        estudios = "Ingeniero Biomedico"
        empleo = "Oracle"

        return render(request,self.template_name,{
            'nombre': nombre,
            'edad': edad,
            'sexo': sexo,
            'estudios': estudios,
            'empleo': empleo
        })