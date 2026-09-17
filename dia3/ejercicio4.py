def mayor_detres(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3
num1=input("ingrese el primer digito ")
n1=int(num1)
num2=input("ingrese el primer digito ")
n2=int(num2)
num3=input("ingrese el primer digito ")
n3=int(num3)
respuesta=mayor_detres(n1,n2,n3)
print("el numero mas grande es: ",respuesta)