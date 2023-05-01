while True:
    numero = int(input("Introduce un número (o introduce 0 para salir): "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        print(numero, "es un número par")
    else:
        print(numero, "es un número impar")