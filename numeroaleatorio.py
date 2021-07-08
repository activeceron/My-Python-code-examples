# Programa que genera un numero aleatorio e involucra al usuario para adiviniarlo
# Python practice ( @laborion)
# https://github.com/activeceron

import random
import os
aleatorio = random.randint(0,100)

print("\t.- JUEVO DEL NÚMERO ALEATORIO -.")

contador=0

while True:
    numero=int(input("Introduzca el numero a adivinar de 0 a 100:"))
    os.system ("cls")
    contador+=1
    if numero> aleatorio:
        print(f"El numero introducido es mayor,inserta uno mas pequeño.\n    Has hecho {contador} intentos")
        
    elif numero<aleatorio:
        print(f"El numero introducido es menor,inserta uno mas grande.\n Has hecho {contador} intentos")
        
    else:
        print(f"¡¡¡Enhorabuena,has acertado!!!,el numero es {aleatorio} y lo  acertado en  {contador} intentos.")

