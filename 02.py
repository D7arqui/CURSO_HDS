Numero1 = float(input("Ingresa el primer número: "))
Numero2 = float(input("Ingresa el segundo número: "))

if Numero2 != 0:
    resultado = Numero1 / Numero2
    print(f"El resultado de la división es: {resultado}")
else:
    print("Error: No es posible dividir entre cero. Inténtalo de nuevo con un divisor distinto de cero.")