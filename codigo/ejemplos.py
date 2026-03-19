#ingresar un numero por teclado y deteterminar si es multiplo de 2,3 o 5

numero = int(input("ingrese un numero: "));
match numero:
    case _ if numero % 2 == 0:
        print("el numero es multiplo de 2");
    case _ if numero % 3 == 0:
        print("el numero es multiplo de 3"); 
    case _ if numero % 5 == 0:
        print("el numero es multiplo de 5");
