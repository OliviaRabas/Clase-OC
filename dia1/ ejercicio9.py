while(True):
    try:
        precio=input("cual es el precio original del producto?")
        precio2=int(precio)
        porcentajep=input("cual es el porcentaje de descuento?")
        porcentaje2=int(porcentajep)
        break
   
    except ValueError:
        print("hubo un error trate de vuelta")

porcentaje3=precio2*porcentaje2/100
print("el total del descuento es de",porcentaje3)
total=precio2-porcentaje3
print("por lo tanto, tu total es de ",total)