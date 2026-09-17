anio_actual=2026
while True:
    try:
        edad_texto =input("¿en que año naciste?")
        edad_numero=int(edad_texto)
        break
    except ValueError:
        print("no se pudo ejecutar trate otra vez ")

edad=(anio_actual-edad_numero)
if edad<18:
    print("eres menor,acceso denegado")
elif edad==18:
    print("eres mayor de edad, puedes pasar")
else :
    print("eres mayor de edad, puedes pasar")