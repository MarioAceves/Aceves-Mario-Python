from django.http import HttpResponse
from django.views import View
from django.shortcuts import render 
import json

#def portafolio(request):
#    return HttpResponse("comptencia")
    

#def funcion1(datos):
#    print(f"mis datos son:")
#    for x in datos:
#        print(x)


#def funcion2(skills):
#    print(f"mis skills son: ")
#    for y in skills:
#        print(y)


#def funcion3(trabajos):
#    print(f"mis trabajos: ")
#    for z in trabajos:
#        print(z)




#funcion1(mis_datos.items())
#funcion2(mis_skills)
#funcion3(mis_trabajos.items())

class VistaDatos(View):
    template_name ="portafolio.html"

    def post(self,request):
        return render(request)
    
    def get(self,request):
        mis_datos = {
            "Nombres": "Mario Alberto",
            "Primer_apelido": "Aceves",
            "Segundo_apellido": "Lopez",
            "Fecha_nacimiento": "9 Agosto 1992",
            "Edad": 30,
            "Celular": 3318629084,
            "Correo": "aceves.mario5@gmail.com",
            "Domicilio": "Calle luna 35",
            "Genero": "Masculino",
            "Objetivo": "Aplicar conocimientos",
            "Salario_esperado": 10000,
        }        

        mis_skills = {
            "habilidades": ("sql", "python", "java", "C++")
        }
        
        

        mis_trabajos = {
            "lugar_trabajo": "Oracle",
            "anio_inicio": 2019,
            "anio_fin": 2023,
            "puesto": "software developer 3"
        }

        cv = {**mis_datos, 
              **mis_skills, 
              **mis_trabajos}
        
        return render(request,self.template_name,cv) 
    