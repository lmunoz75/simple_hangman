# -*- coding: utf-8 -*-
from random import choice
import os
import time

lista_palabras = ['velador', 'celada', 'zapato', 'camisa', 'verguenza', 'camion', 'respeto', 'sendero', 'semana', 'rabioso', 
                  'recibir', 'amistad', 'genero', 'adivino', 'sentido', 'ordenador', 'circular', 'rectangulo', 'cocina', 
                  'piramide', 'medicina', 'palanca', 'resfrio', 'cebolla', 'tomate', 'tractor', 'patineta', 'amarillo']

# ---------- Funciones ---------------
def show_hangman(idx):
# Imprime el esquema del ahorcado en el terminal
    hangman = [
        """
                 ------------
                 |          |
                 |          O
                 |
                 |
                 |
                 |
                 |
            ----------
        """, 
        """
                 ------------
                 |          |
                 |          O
                 |          |
                 |
                 |
                 |
                 |
            ----------
        """, 
        """
                 ------------
                 |          |
                 |          O
                 |         /|
                 |
                 |
                 |
                 |
            ----------
        """, 
        """
                 ------------
                 |          |
                 |          O
                 |         /|\\
                 |
                 |
                 |
                 |
            ----------
        """, 
        """
                 ------------
                 |          |
                 |          O
                 |         /|\\
                 |          |
                 |
                 |
                 |
            ----------
        """, 
        """
                 ------------
                 |          |
                 |          O
                 |         /|\\
                 |          |
                 |         /
                 |
                 |
            ----------
        """, 
        """
                 ------------
                 |          |
                 |          O
                 |         /|\\
                 |          |
                 |         / \\
                 |
                 |
            ----------
        """]
        
    print(hangman[idx])


def index_letras(palabra, letra):
    # Retorna una lista con los indices de ocurrencia de una letra en una palabra
    
    #lista = []
    #for idx in len(palabra):
    #    if palabra[idx].upper() == letra.upper():
    #        lista.upper(idx)
    
    return [idx for idx in range(len(palabra)) if palabra[idx].upper() == letra.upper()]


# ------ Script ------
# Seleccionamos la palabra a adivinar y la palabra a rellenar
palabra_adivinar = choice(lista_palabras).upper()
palabra_actual = ["_"] * len(palabra_adivinar)

# Condiciones generales del juego
num_intentos = 0
max_intentos = 6
win_game = False

# Mientras no haya superado el numero de intentos y no haya ganado el juego...
while num_intentos < max_intentos and not win_game:
    # ...se muestra la pantalla del juego
    os.system('cls')
    print("{:^45}".format("EL AHORCADO"))
    print("{:^45}".format("==========="))
    show_hangman(num_intentos)
    print()
    print("Palabra:", " ".join(palabra_actual))
    print()
    
    # Se pide al usuario que ingrese una letra o palabra
    letra_palabra = input("Letra o palabra : ")
    
    # Si es una letra se verifica si es parte de la palabra a adivinar...
    if len(letra_palabra) == 1 and letra_palabra.upper() in palabra_adivinar:
        indices = index_letras(palabra_adivinar, letra_palabra)
        for indice in indices:
            palabra_actual[indice] = letra_palabra.upper()
            
        # ... para luego ver su se completo la palabra
        if "".join(palabra_actual) == palabra_adivinar:
            print("Correcto! ->", palabra_adivinar)
            win_game = True
            
    # Y que sucede si se ingresa una palabra?
    elif letra_palabra.upper() == palabra_adivinar:
        print("Correcto! ->", palabra_adivinar)
        win_game = True
    
    # Si la letra no esta en la palabra y la palabra no es la palabra
    # a adivinar, se actualiza el contador de jugadas
    else:
        print("No hay coincidencia...")
        num_intentos += 1
        time.sleep(1)
        
        
# Si se rompe el lazo, verificar por que
if not win_game:
    os.system('cls')
    print("{:^45}".format("EL AHORCADO"))
    print("{:^45}".format("==========="))
    show_hangman(num_intentos)
    print()
    print("No hay mas intentos :(")
