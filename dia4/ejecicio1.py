saldo=1000
def verificar_pin(pin):
    if pin=="1234":
        return True
    else:
        return False
    
pin=input("ingrese pin: ")  

def retirar(cantidad):
    global saldo
    if saldo>cantidad:
        saldo=saldo-cantidad
        print("retiro exitoso")
        return saldo
    else:
        print("fondos insuficientes")   
        return saldo
      

if verificar_pin(pin):
    print("acceso concedido, su saldo es: ",saldo)
  
    try:
        cantidad=int(input("cuanto desea retirar? "))
        print("su saldo actual es de: ",retirar(cantidad))

    except ValueError:
        print("error,ingrese un numero valido")

else:
    print("PIN incorrecto, policia en camino")


