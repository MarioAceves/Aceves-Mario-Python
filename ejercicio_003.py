#definir password correcta
password = "welcome"

#preguntar contrasenia
password_usuario = input("Teclee la contraseña correct? ")

while password_usuario != password:
    print("Contraseña incorrecta")
    password_usuario = input("Teclee la contraseña correct? ")
else:
    print("Contraseña correcta")
