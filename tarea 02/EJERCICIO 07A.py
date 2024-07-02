from collections import Counter
def contar_palabras(cadena):
    palabras = cadena.split()
    contador = Counter(palabras)
    return contador
def palabra_mas_repetida(diccionario):
    palabra, frecuencia = diccionario.most_common(1)[0]
    return (palabra, frecuencia)
cadena = "hola hola mundo mundo hola"
diccionario_frecuencias = contar_palabras(cadena)
print("Diccionario de frecuencias:", diccionario_frecuencias)

palabra_repetida, frecuencia = palabra_mas_repetida(diccionario_frecuencias)
print(f"La palabra más repetida es '{palabra_repetida}' con una frecuencia de {frecuencia}.")