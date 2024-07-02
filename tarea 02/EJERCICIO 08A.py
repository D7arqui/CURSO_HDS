def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a
def calcular_mcm(a, b):
    return abs(a*b) // calcular_mcd(a, b)

numero1 = 24
numero2 = 36

mcd_numeros = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd_numeros}")

mcm_numeros = calcular_mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es: {mcm_numeros}")