print("hola")
contrasena = input("ingresa la contrasena: ")


for i in range(len(contrasena)>= 8):
    if (contrasena[i].isupper()) and (contrasena[i].islower()): 
            print("cunple con las condiciones 1 ")
    else:
        print("opcion denegada")


#and contrasena[i].isdigit():