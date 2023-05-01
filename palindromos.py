palabras = []

for i in range(5):
    palabra = input("Introduce una palabra: ")
    palabras.append(palabra)

print("Palabras palíndromas:")
for palabra in palabras:
    if palabra == palabra[::-1]:
        print(palabra)