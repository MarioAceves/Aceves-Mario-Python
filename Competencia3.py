def funcion1(datos):
    print(f"mis datos son:")
    for x in datos:
        print(x)


def funcion2(skills):
    print(f"mis skills son:")
    for y in skills:
        print(y)


def funcion3(trabajos):
    print(f"mis trabajos: ")
    for z in trabajos:
        print(z)



mis_datos = {
        "nombres": "Mario Alberto",
        "primer_apelido": "Aceves",
        "segundo_apellido": "Lopez",
        "fecha_nacimiento": "9 Agosto 1992",
        "edad": 30,
        "celular": 3318629084,
        "correo": "aceves.mario5@gmail.com",
        "domicilio": "Calle luna 35",
        "genero": "Masculino",
        "objetivo": "Aplicar conocimientos",
        "salario_esperado": 10000,
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
