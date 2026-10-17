#8.  Índice de masa corporal (IMC):
#Pide al usuario su peso (en kilogramos) y su altura (en metros). 
#Calcula su IMC (IMC = peso / (altura ** 2)) e imprime el resultado.

def peso():
    peso = float(input("ingresa el peso: "))
    altura = float(input("ingresa la altura: "))
    IMC = (peso / (altura ** 2))

    return(f"su IMC es de {IMC: .2f}")
print(peso())
