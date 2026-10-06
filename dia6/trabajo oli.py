numeros=[]
par=[]
impar=[]
try:
    while True:
        num=(int(input("por favor, ingrese un num ")))
        numeros.append(num)
except ValueError:
    for indice in numeros:
        resto=indice%2
        if resto==0:
            par.append(indice)
        else:
            impar.append(indice)            
    print( "pares",par,"impares",impar)