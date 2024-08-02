while True:
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu sexo (H para hombre, M para mujer): ")
    if sexo == "M" and nombre[0].upper() < "M" or sexo == "H" and nombre[0].upper() > "N":
        grupo = "A"
    else:
        grupo = "B"
    print(f"Perteneces al grupo {grupo}")
    continuar = input("¿Quieres comprobar otro nombre y sexo? (s/n): ")
    if continuar.lower() != "s":
        break