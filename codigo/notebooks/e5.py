
envio = {
    "local": [500 , 1000, 2000],
    "regional": [1000, 2500, 5000],
    "nacional": [2000, 4500, 8000]
}
zonas = ["local", "regional", "nacional"]
print('ingres el peso del paquete:')
peso = float(input())
print("ingrese la zona de destino")
zona = (input())
while zona not in zonas:
    print("zona no valida")
    zona = (input())
else:
    if(peso <= 1):
        indice = 0
    elif(peso <= 5):
        indice = 1
    else:
        indice = 2
precioFinal = envio[zona][indice]
print(precioFinal)
    
