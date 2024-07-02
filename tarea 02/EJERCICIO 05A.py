import statistics
def calcular_estadisticas(muestra):
    media = statistics.mean(muestra)
    varianza = statistics.variance(muestra)
    desviacion_tipica = statistics.stdev(muestra)
    
    return {'media': media, 'varianza': varianza, 'desviacion_tipica': desviacion_tipica}
muestra_numeros = [2, 4, 6, 8, 10]
estadisticas_muestra = calcular_estadisticas(muestra_numeros)
print("Estadísticas de la muestra:", estadisticas_muestra)