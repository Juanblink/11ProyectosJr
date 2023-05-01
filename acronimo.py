frase = input("Ingrese el significado completo: ")

acronimo = ""
for palabra in frase.split():
    acronimo += palabra[0].upper()

print("El acrónimo es:", acronimo)