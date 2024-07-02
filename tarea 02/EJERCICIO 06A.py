def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

numero_decimal = 25
numero_binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {numero_binario}")
numero_binario = "11001"
numero_decimal = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {numero_decimal}")