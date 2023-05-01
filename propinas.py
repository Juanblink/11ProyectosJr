factura_total = float(input("¿Cuál es la factura total de hoy, por favor? "))
proporciones = [0.18, 0.20, 0.25]

for prop in proporciones:
    propina = factura_total * prop
    total = factura_total + propina
    print(f"La propina aplicando el {int(prop*100)}% es ${round(propina, 2)}, que contabiliza un total de ${round(total, 2)}")