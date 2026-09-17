def es_par(numero):
    resto=numero%2
    if resto==0:
        return "true"
    else:
        return "false"
num=input("ingrese un numero ")
numero=int(num)
respuesta=es_par(numero)
print("es par? ",respuesta)