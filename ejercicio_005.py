#Se define del diccionario
Frutas = {
    "platano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

fruta = input("Que fruta desea comprar? ")
kilos = int(input(f"cuantos kilos desea de {fruta} ? " ))

if fruta in Frutas:
    precio = Frutas[fruta]*kilos
    print(f"El total a pagar es {precio} ")
else:
    print(f"No tenemos {fruta} actualmente")
