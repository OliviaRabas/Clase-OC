num1=input("ingrese el primer numero")
numero1=int(num1)
num2=input("ingrese el segundo numero")
numero2=int(num2)
if numero1==0:
    print("error, no se puede dividir por 0")
elif numero2==0:
    print("error, no se puede dividir por 0")
else:
    patata=numero1/numero2
    print(patata)
