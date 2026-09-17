def crear_email(nombre,apellido):
    return f"{nombre}.{apellido}@empresa.com"
nombre=input("ingrese su nombre ")
apellido=input("ingrese su apellido ")
respuesta=crear_email(nombre,apellido)
print("tu email es: ",respuesta)