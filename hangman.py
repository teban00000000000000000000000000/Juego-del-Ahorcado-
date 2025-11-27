"""
Hangman game - Assignment deliverable
Implements:
- Use of conditionals and loops
- Repetitive structures (while, for)
- Comments explaining complex parts
- Simple CLI interface for demonstration
"""

import random
import sys

# Word list (you can expand this or load from a file)
WORDS = [
    "python", "programacion", "computadora", "seguridad", "algoritmo",
    "variable", "funcion", "bucles", "condicional", "desarrollo"
]

def escoger_palabra():
    """Escoge una palabra aleatoria de la lista WORDS."""
    return random.choice(WORDS).upper()

def mostrar_tablero(palabra, letras_adivinadas, intentos_restantes):
    """Muestra el estado actual del juego: palabra con guiones, letras falladas e intentos."""
    display = " ".join([c if c in letras_adivinadas else "_" for c in palabra])
    print("\nPalabra: ", display)
    print("Letras adivinadas:", " ".join(sorted(letras_adivinadas)))
    print("Intentos restantes:", intentos_restantes)

def solicitar_letra(letras_adivinadas):
    """Pide al usuario una letra válida que no haya sido ingresada antes."""
    while True:
        entrada = input("Ingresa una letra: ").strip().upper()
        if len(entrada) != 1 or not entrada.isalpha():
            print("Por favor ingresa solo UNA letra.")
            continue
        if entrada in letras_adivinadas:
            print("Ya ingresaste esa letra. Intenta otra.")
            continue
        return entrada

def juego_ahorcado():
    """Lógica principal del juego usando bucles y condicionales."""
    palabra = escoger_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6  # número de errores permitidos

    # Bucle principal: continúa hasta ganar o quedarse sin intentos
    while True:
        mostrar_tablero(palabra, letras_adivinadas, intentos_restantes)

        # Verificar victoria
        if all(c in letras_adivinadas for c in palabra):
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break

        if intentos_restantes <= 0:
            print("\nTe has quedado sin intentos. La palabra era:", palabra)
            break

        letra = solicitar_letra(letras_adivinadas)
        letras_adivinadas.add(letra)

        # Si la letra no está en la palabra, restar intento
        if letra not in palabra:
            intentos_restantes -= 1
            print(f"La letra {letra} no está en la palabra.")
        else:
            print(f"¡Bien! La letra {letra} está en la palabra.")

    # Al final, preguntar si quiere jugar de nuevo
    jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (S/N): ").strip().upper()
    if jugar_de_nuevo == "S":
        juego_ahorcado()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

if __name__ == "__main__":
    try:
        juego_ahorcado()
    except KeyboardInterrupt:
        print("\nJuego interrumpido. ¡Adiós!")
        sys.exit(0)
