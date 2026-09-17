def puede_votar(edad):
    if edad>=18:
        return "puede votar"
    else:
        return "no puede votar"
eda=input("ingresar edad ")
edad=int(eda)
respuesta=puede_votar(edad)
print(respuesta)