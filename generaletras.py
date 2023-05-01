
canciones = {
    "Baby by Bieber": "Oh, for you, I would've done whatever",
    "Hotline Bling by Drake": "You used to call me on my",
    "Flawless by Beyonce": "Your challengers are a young group from Houston",
    "Fall by Eminem": "You know, everybody's been tellin' me what they think about me for the last few months",
    "Shape of You by Ed Sheeran": "The club isn't the best place to find a lover",
    "Sorry by Justin Bieber": "You gotta go and get angry at all of my honesty",
    "Roar by Katy Perry": "I used to bite my tongue and hold my breath",
    "Blank Space by Taylor Swift": "Nice to meet you, where you been?",
    "Uptown Funk by Mark Ronson ft. Bruno Mars": "This hit, that ice cold",
    "One More Night by Maroon 5": "You and I go hard at each other like we're going"
}


print("Bienvenido, por favor, selecciona una canción de este top de 10 canciones:\n")
for cancion in canciones:
    print(cancion)
    

while True:
    eleccion = input("\nPor favor, introduce el nombre de la canción que quieres ver la letra: ")
    if eleccion in canciones:
        print(f"\nHas seleccionado '{eleccion}'. Te mostramos la letra a continuación:\n")
        print("-------", eleccion, "-------")
        print(canciones[eleccion])
        break
    elif eleccion == "*":
        print("\nHasta luego! Gracias por jugar.")
        break
    else:
        print("La canción que has elegido no está en la lista. Por favor, seleccione otra o pulse * para salir.")