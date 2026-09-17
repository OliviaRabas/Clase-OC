frase=input("dime una frase ")
cont=0
for indice in frase:
    if indice in "AaEeIiOoUu":
        cont=cont+1
print("cantidad de vocales ",cont)