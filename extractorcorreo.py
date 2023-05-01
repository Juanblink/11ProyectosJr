import re

# pedir dirección de correo electrónico al usuario
email = input("Introduce tu dirección de correo electrónico: ")

# extraer el nombre de dominio de la dirección de correo electrónico
match = re.search(r"@[\w.]+", email)
if match:
    domain = match.group()[1:]  # eliminar el símbolo '@'
else:
    print("Dirección de correo electrónico inválida.")
    exit()

# lista de dominios populares
popular_domains = ["gmail.com", "yahoo.com", "hotmail.com"]

# determinar si el dominio es personalizado o popular
if domain in popular_domains:
    print(f"Hola {email.split('@')[0].title()}, estoy viendo que tu email está registrado con {domain}. ¡Eso es genial!")
else:
    print(f"Hola {email.split('@')[0].title()}, estoy observando que estás utilizando un dominio personalizado de {domain}. ¡Impresionante!")