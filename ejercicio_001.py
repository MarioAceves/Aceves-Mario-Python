#Obtener valores
Nombre = input('¿Cuál es tu nombre? ')
PrimerApellido = input('¿Cuál es tu primer apellido? ')
SdoApellido = input ('¿Cuál es tu segundo apellido? ')
FechaNac = int(input('¿En que anio naciste? '))
Mesyanio = input('¿En que mes y dia naciste? mm-dd ')
anio_actual = 2022
Edad = anio_actual - FechaNac
print("")

#Obtener Vocales
#def cont_vocal(frase):
#    contador = 0
#    for letra in frase:
#        if letra.lower() in "aeiou":
#        contador += 1
#    return contador

#imprimir valores
#A
print('Este es tu nombre en mayusculas: ',  Nombre.upper())
#B
print('Este es tu nombre en minusculas: ',  Nombre.lower())
#C
print('Tu fecha de nacimiento: ', Mesyanio, FechaNac )
#D
print('Esta es tu edad:', Edad )
#E
#print('Tu nombre completo tiene', vocales(Nombre) + vocales(PrimerApellido) + vocales(SdoApellido)  ,'vocales')
#F
print('Tu nombre completo tiene ', len(Nombre) + len(PrimerApellido) + len(SdoApellido),' Letras')
#G
#print('Tu edad es un caracter de tipo numero?')
#H
#print('Tu nombre completo es un caracter de tipo alfanumerico? ')
#I
print('Tu edad en 10 nios sera: ', Edad + 10)
#J
print('La media de tu edad actual y tu edad en 20 anios es ', (Edad + 20)/2)
