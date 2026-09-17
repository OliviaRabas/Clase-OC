def areacir(radio):
    area=3.1416*radio*radio
    return area
rad=input("ingrese el radio del circulo ")
radio=int(rad)
respuesta=areacir(radio)
print("el area de tu circulo es: ",respuesta)