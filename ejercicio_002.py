#Obtener nombre y sexo del usuario
Nombre=input('Cual es su nombre? ')
Sexo=input('Cual es su sexo (Hombre o Mujer)? ')

if Nombre.lower() < "M":
    if Sexo.lower() == "mujer":
        print("Grupo A")
    else:
        print("Grupo B")
else:
    if Sexo.lower() == "hombre":
        print("Grupo a")        
    else:
        print("Grupo b")
