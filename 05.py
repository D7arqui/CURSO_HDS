while True:
    edad = int(input("Ingresa la edad del cliente: "))
    if edad < 4:
        precio = 0
    elif edad >= 4 and edad <= 18:
        precio = 10
    else:
        precio = 20
    print(f"El precio de entrada para el cliente de {edad} años es de {precio} soles.")
    continuar = input("¿Deseas calcular el precio de entrada para otro cliente? (s/n): ")
    if continuar.lower() != "s":
        break