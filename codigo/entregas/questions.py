import random
#7.C
words = {
    "lenguaje": ["python", "programa", "funcion", "bucle"]
    ,"datos": ["entero", "cadena", "lista"]
}
#7.C
categoria = input("Selecciona una categoría: lenguaje o datos: ")
#7.C
while categoria not in words:
    print("Categoría no válida. Por favor, selecciona 'lenguaje' o 'datos'.")
    categoria = input("Selecciona una categoría: lenguaje o datos: ")
#7.C
word = random.choice(words[categoria])
guessed = []
attempts = 6
puntaje = 0
print("¡Bienvenido ala Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        #7.B
        puntaje += 6
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    #7.A
    if len(letter) != 1:
        print("Por favor, ingresá una letra válida.")
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        #7.B
        puntaje -= 1
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    #7.B
    puntaje = 0
print(f"Tu puntaje final es: {puntaje}")