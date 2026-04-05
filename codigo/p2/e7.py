import random
print("ingrese los nombres de los participantes separados por comas")
nombres = input()
print(nombres)
nombres = nombres.split(", ")
nombres = list(dict.fromkeys(nombres))
print(nombres)
jugadores = len(nombres)
random.shuffle(nombres) #mezcla los jugadores
jugadoresA = nombres[1:] + [nombres[0]] #mueve el primer jugador al final
for i in range(len(nombres)):
    print(nombres[i], "-", jugadoresA[i])

    
                            

