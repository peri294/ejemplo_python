print('ingrese un mensaje')
mensaje = input()
print("ingrese el desplazamiento")
desplazamiento = int(input())
mensajeCifrado = ""
for letter in mensaje:
    mensajeCifrado = mensajeCifrado + (chr(ord(letter) + desplazamiento))
print(mensajeCifrado)
mensaje =""
for letter in mensajeCifrado:
    mensaje = mensaje + (chr(ord(letter) - desplazamiento))
print(mensaje)