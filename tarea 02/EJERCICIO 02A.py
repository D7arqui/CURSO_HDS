import math
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area
def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen
radio_circulo = 5
area_circulo = calcular_area_circulo(radio_circulo)
print("El área del círculo con radio", radio_circulo, "es:", area_circulo)

radio_cilindro = 3
altura_cilindro = 8
volumen_cilindro = calcular_volumen_cilindro(radio_cilindro, altura_cilindro)
print("El volumen del cilindro con radio", radio_cilindro, "y altura", altura_cilindro, "es:", volumen_cilindro)