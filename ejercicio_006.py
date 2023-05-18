#Funcion para obtener area
def area(radio):
    pi = 3.1416
    return pi*radio**2

#funcion para obtener volume
def volumen(radio,altura):
    volumen = area(radio)*altura
    return volumen
  
print(f'Area = {area(5)}')
print(f'Volumen = {volumen(5,10)}')
