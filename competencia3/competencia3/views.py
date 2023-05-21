from django.http import HttpResponse
from django.views import View
from django.shortcuts import render 
import json

def portafolio(request):
    return HttpResponse("comptencia")
    

def funcion1(datos):
    print(f"mis datos son:")
    for x in datos:
        print(x)


def funcion2(skills):
    print(f"mis skills son: ")
    for y in skills:
        print(y)


def funcion3(trabajos):
    print(f"mis trabajos: ")
    for z in trabajos:
        print(z)



mis_datos = {
        "Nombres:": "Mario Alberto",
        "Primer apelido:": "Aceves",
        "Segundo apellido:": "Lopez",
        "Fecha Nacimiento:": "9 Agosto 1992",
        "Edad:": 30,
        "Celular:": 3318629084,
        "Correo:": "aceves.mario5@gmail.com",
        "Domicilio:": "Calle luna 35",
        "Genero:": "Masculino",
        "Objetivo:": "Aplicar conocimientos",
        "Salario esperado:": 10000,
  }        

mis_skills = ("sql", "python", "java", "C++")

mis_trabajos = {
        "luger_trabajo": "Oracle",
        "año inicio": 2019,
        "año fin": 2023,
        "puesto": "software developer 3"
    }

funcion1(mis_datos.items())
funcion2(mis_skills)
funcion3(mis_trabajos.items())

class VistaDatos(View):
    template_name ="portafolio.html"

    def post(self,request):
        return render(request)
    
    def get(self,request):
        x= mis_datos.items()
        y= mis_skills 
        z= mis_trabajos.items()
        return render(request,self.template_name,{
            'datos': x,
            'skills': y,
            'trabajos': z
        }) 
    