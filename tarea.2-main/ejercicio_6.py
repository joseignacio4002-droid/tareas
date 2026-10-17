contador = 0

palabra = input("ingresa una oracion o palabra: ").lower()

vocal = ['a', 'e', 'i', 'o', 'u']

for letra in palabra:
    if letra in vocal:
        contador += 1

print(f"hay {contador}")
