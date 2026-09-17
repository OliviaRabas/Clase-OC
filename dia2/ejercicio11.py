import random
secreto = random.randint(1, 100)
adivinado = False  
print( "He pensado un número del 1 al 100. ¿Puedes adivinarlo?")
while adivinado == False:
    num=input("ingrese un numero ")
    numero=int(num)
    if numero==secreto:
        print("ganaste")
        break
    elif numero>secreto:
        print("no,el numero es menor")
    else:
        print("el numero es mayor")