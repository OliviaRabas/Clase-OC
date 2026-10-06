par=[]
impar=[]
try:
    while True:
        numero=int(input("ingresar numero "))
        num=numero%2
        if num==0:
            par.append(numero)
        else:
            impar.append(numero)
except ValueError:
    print("pares:",par)
    print("impares:",impar)