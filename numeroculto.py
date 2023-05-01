import random

numero_oculto = random.randint(1, 50)
intentos = 0

while True:
    intentos += 1
    
    respuesta = input("Adivina el número oculto entre 1 y 50: ")
    
    if not respuesta.isdigit():
        print("Error: La respuesta debe ser un número entero.")
        continue
    
    respuesta = int(respuesta)
    
    if respuesta < 1 or respuesta > 50:
        print("Error: La respuesta debe estar entre 1 y 50.")
        continue
    
    if respuesta == numero_oculto:
        print("¡Felicidades, has acertado en", intentos, "intentos!")
        break
    
    opcion = input("Respuesta incorrecta. ¿Quieres seguir intentándolo? (s/n): ")
    
    if opcion.lower() != "s":
        break