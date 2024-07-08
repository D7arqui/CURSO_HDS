def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    return (palabra_max, frecuencia_max)
cadena = input("Ingresa una cadena de caracteres: ")
diccionario = contar_palabras(cadena)
palabra_maxima, frecuencia_maxima = palabra_mas_repetida(diccionario)
print(f"Diccionario de palabras y frecuencias: {diccionario}")
print(f"La palabra más repetida es '{palabra_maxima}' con una frecuencia de {frecuencia_maxima}.")