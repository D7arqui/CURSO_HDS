list=[]
for i in range(6):
  list.append(int(input('Ingrese número ganador: ')))
list.sort()
print('Números ganadores: ')
print(*list, sep=', ')
print(f'Números ganadores: {", ".join(str(x) for x in list)}')
print('Números ganadores: {} {} {} {} {} {}'.format(*list))