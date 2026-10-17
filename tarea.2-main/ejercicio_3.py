contador = 1

print("calculdora factorial")
numero = int(input("ingresa el numero: "))

for i in range(1, numero + 1):

    contador *= i
    
print(f" es {contador}")