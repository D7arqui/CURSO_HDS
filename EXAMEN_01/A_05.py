import math
def calcular_estadisticos(numeros):
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media)**2 for x in numeros) / len(numeros)
    desviacion_tipica = math.sqrt(varianza)
    return {
        'media': media,
        'varianza': varianza,
        'desviacion_tipica': desviacion_tipica
    }
muestra = [5, 10, 15, 20, 25]
estadisticos = calcular_estadisticos(muestra)
print(estadisticos)
