numero = int(input("ingres el numero: "))

'''
if numero > 0:
    for i in range(numero + 1):
        print(f"{i}")
        for j in range(i + 1):
            print(f"{j}", end=" ")
else:
print("el numero tiene que ser positivo)
'''

if numero > 0:
    for i in range(numero, 0, - 1):
       # print(f"{i}")
        for j in range(i + 1):
            print(f"{j}", end=" ")