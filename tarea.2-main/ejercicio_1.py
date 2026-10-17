# 1. Adivina el número:

#Crea un programa que genere un número aleatorio entre 1 y 100. 
#Luego, pide al usuario que adivine el número. 
#El programa debe dar pistas al usuario (mayor o menor) hasta que adivine el número.

import random
numero_secreto = random.randint(1, 100)
print("bienvenido al juego tienes que adivinar un numero del 1 al 100")
intento = int(input("ingresa tu respuesta: "))

while numero_secreto != intento:
    if numero_secreto > intento:
        print("El número secreto es MAYOR: ")
    else:
        print("El número secreto es MENOR: ")
    intento = int(input("ingresa tu nueva respuesta: "))
print("fin del codigo")
