def calcular_precio_final(precio,descuento):
    preciofinal=(precio*descuento/100)+precio
    return preciofinal
pre=input("ingrese el precio ")
precio=int(pre)
des=input("ingrese porcentaje de descuento ")
descuento=int(des)
respuesta=calcular_precio_final(precio,descuento)
print("el precio total es de ",respuesta)