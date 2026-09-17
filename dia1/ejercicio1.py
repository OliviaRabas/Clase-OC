while(True):
    try:
    numero=input("ingresa numero ")
except ValueError:
    print("lo siento hubo un error ")
pasadon=int(numero)
division=pasadon%2
if division==0:
    print("es par")
else:
    print("es impar")