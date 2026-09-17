precio={
    "manzana":100,
    "banana":50,
    "naranja":80
}
nombre=input("ingresar que fruta desea ")
peso=input("cuantos kilos quiere? ")
pesokg=int(peso)
precioto=precio.get(nombre)*pesokg
print("precio total: ",precioto)