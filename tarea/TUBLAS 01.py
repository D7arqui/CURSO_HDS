########### tUPLAS

#Utilizando paréntesis:
mi_tupla = (1, 2, 3, 4)

#Utilizando la función tuple():
mi_lista = [1, 2, 3, 4]
mi_tupla = tuple(mi_lista)

#Sin paréntesis:
mi_tupla = 1, 2, 3, 4

###
mi_tupla = (1,)

# Imprime 3
mi_tupla = (1, 2, 3, 4)
print(mi_tupla[2]) 

# Imprime 3
mi_tupla = (1, 2, 3, 4)
indice = 2
print(mi_tupla[indice])

# Imprime 3
mi_tupla = (1, 2, 3, 4)
print(mi_tupla[-2])

# Imprime (2, 3)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[1:3])

# Imprime (1, 2, 3)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[:3])

# Imprime (3, 4, 5)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[2:])

# Imprime (1, 3, 5)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[::2])

# Imprime (3, 4)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[-3:-1])

# Imprime (4, 2)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[-2::-2])

mi_tupla = (1, 2, 3, 4)
print(2 in mi_tupla) # Imprime True
print(5 in mi_tupla) # Imprime False

mi_tupla = (1, 2, 3, 4)
print(2 not in mi_tupla) # Imprime False
print(5 not in mi_tupla) # Imprime True