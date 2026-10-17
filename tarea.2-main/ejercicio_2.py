import random
print("bienvenido al programa")
print("elije entre piedra, papel o tijera")
palabra = str(input("ingresa la respuestas: ")).lower()

respuesta = ['piedra', 'papel', 'tijera']
palabra_elejida = random.choice(respuesta)

if palabra == palabra_elejida:
    print(f"empate {palabra_elejida}")

elif palabra == 'piedra' and palabra_elejida == 'tijera':
    print(f"ganaste la pc eligio {palabra_elejida}")

elif palabra == 'piedra' and palabra_elejida == 'papel':
    print(f"perdiste la pc eligio {palabra_elejida}")

elif palabra == 'tijera' and palabra_elejida == 'papel':
   print(f"ganaste la pc eligio {palabra_elejida}")

elif palabra == 'tijera' and palabra_elejida == 'piedra':
    print(f"perdiste la pc eligio {palabra_elejida}")

elif palabra == 'papel' and palabra_elejida == 'piedra':
    print(f"ganaste la pc eligio {palabra_elejida}")

elif palabra == 'papel' and palabra_elejida == 'tijera':
   print(f"perdiste la pc eligio {palabra_elejida}")
else:
    print("opcion invalida")