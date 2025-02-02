

import random


def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript','java','angular','django','tensorflow', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"

    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La cantidad de letras de la palabra secreta es:", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra del abecedario.")
        elif adivinanza in letras_adivinadas:
            print("Ya usaste esa letra, proba con otra.")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"¡Bien! '{adivinanza}' está en la palabra. Te queda una menos.")
            else: 
                intentos -=1
                print(f"¡Lastima! '{adivinanza}' no está en la palabra secreta.")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Felicidades, ganaste! La palabra secreta es: '{palabra_secreta}'")
    
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Lo sentimos mucho, te quedaste sin intentos. La palabra secreta era '{palabra_secreta}'")

juego_ahorcado()




