suma =0
precio = -1
while (precio != 0):
    precio = float(input("ingrese el precio del producto: "))
    if (precio == 0):
        break
    suma += precio
print("el total a pagar es: ", suma)