edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresa tus ingresos mensuales en soles: "))

if edad >= 18 and ingresos >= 2000:
    print("Debes pagar impuestos.")
else:
    print("No estás obligado a pagar impuestos en este momento.")
