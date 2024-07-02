def calcular_media(muestra):
    media = sum(muestra) / len(muestra)
    return media
muestra_numeros = [10, 20, 30, 40, 50]
media_muestra = calcular_media(muestra_numeros)
print("La media de la muestra es:", media_muestra)