#Obtener nombre y sexo del usuario
Nombre=input('Cual es su nombre? ')
Sexo=input('Cual es su sexo (Hombre o Mujer)? ')

if Sexo.lower() == "mujer":
    if Nombre.lower() < "m":
        print("Grupo A")
    else:
        print("Grupo B")
else:
    if Nombre.lower() > "n":
        print("Grupo A")        
    else:
        print("Grupo B")
