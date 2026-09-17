def minutos_a_horas(minutos):
    minuts=minutos%60
    horas=minutos//60
    return horas,"horas y",minuts," minutos"
min=input("ingrese la cantidad de minutos ")
minutos=int(min)
respuesta=minutos_a_horas(minutos)
print(respuesta)