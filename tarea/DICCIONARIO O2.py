#Creación de diccionarios en Python
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
print(estudiantes) # {'Juan': 16, 'Ana': 18, 'Luis': 17}

estudiantes = dict([('Juan', 16), ('Ana', 18), ('Luis', 17)])
print(estudiantes) # {'Juan': 16, 'Ana': 18, 'Luis': 17}

#Agregar, modificar y eliminar elementos
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
estudiantes['Maria'] = 15
print(estudiantes) # {'Juan': 16, 'Ana': 18, 'Luis': 17, 'Maria': 15}

estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
estudiantes['Ana'] = 19
print(estudiantes) # {'Juan': 16, 'Ana': 19, 'Luis': 17}

estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
del estudiantes['Juan']
print(estudiantes) # {'Ana': 18, 'Luis': 17}

#Acceder a los elementos
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
print(estudiantes['Ana']) # 18

estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
print(estudiantes.get('Maria', 'No existe')) # 'No existe'

#Iterar a través de los elementos
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
for clave in estudiantes:
    print(clave, estudiantes[clave])

estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
for clave, valor in estudiantes.items():
    print(clave, valor)

#Verificación de pertenencia
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
if 'Ana' in estudiantes:
    print('Ana es un estudiante')

estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
print(len(estudiantes)) # 3