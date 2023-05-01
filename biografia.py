nombre = input("¿Cuál es su nombre? ")
while not nombre.isalpha():
    nombre = input("Entrada incorrecta. Por favor, ingrese su nombre correctamente: ")

edad = input("¿Cuál es su edad? ")
while not edad.isnumeric():
    edad = input("Entrada incorrecta. Por favor, ingrese su edad correctamente: ")

direccion = input("¿Cuál es su dirección? ")
while not direccion:
    direccion = input("Entrada incorrecta. Por favor, ingrese su dirección correctamente: ")

trabajo = input("¿En qué trabaja? ")
while not trabajo:
    trabajo = input("Entrada incorrecta. Por favor, ingrese su trabajo correctamente: ")

print("\nResumen de la información personal:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Dirección:", direccion)
print("Trabajo:", trabajo)