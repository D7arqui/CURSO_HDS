def calcular_cuadrados(muestra):
    return [numero ** 2 for numero in muestra]
muestra_numeros = [2, 4, 6, 8, 10]
cuadrados_muestra = calcular_cuadrados(muestra_numeros)
print("Lista de cuadrados de la muestra:", cuadrados_muestra)