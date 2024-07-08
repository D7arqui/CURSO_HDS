def contar_apariciones(lista_palabras, palabra_buscada):
    contador = lista_palabras.count(palabra_buscada)
    return contador
lista_palabras = ["david", "fredy", "rodrich", "yenifer", "david"]
palabra_buscada = input("Ingresa una palabra para buscar en la lista: ")
apariciones = contar_apariciones(lista_palabras, palabra_buscada)
print(f"La palabra '{palabra_buscada}' aparece {apariciones} veces en la lista de palabras.")