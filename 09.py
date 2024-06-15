frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra para buscar en la frase: ")
contador = 0
for caracter in frase:
    if caracter.lower() == letra.lower():
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la frase proporcionada.")