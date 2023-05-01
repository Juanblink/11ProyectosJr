import random

victorias = 0
derrotas = 0

while True:
    print("Seleccione una opción: ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("4. Salir")
    
    opcion = input("Ingrese su elección: ")
    if opcion == "4":
        break
    
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida. Por favor, ingrese una opción válida.")
        continue
    
    opcion_jugador = int(opcion)
    opcion_computadora = random.randint(1, 3)
    
    if opcion_jugador == opcion_computadora:
        print("Empate.")
    elif (opcion_jugador == 1 and opcion_computadora == 3) or \
         (opcion_jugador == 2 and opcion_computadora == 1) or \
         (opcion_jugador == 3 and opcion_computadora == 2):
        print("¡Ganaste!")
        victorias += 1
    else:
        print("Perdiste.")
        derrotas += 1
    
print("Resumen de resultados:")
print("Victorias:", victorias)
print("Derrotas:", derrotas)