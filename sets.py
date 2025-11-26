my_set = {}
print(type(my_set)) #nos indicara que es un diccionario

my_set = {'hola','agua','python'}
print(type(my_set)) #ahora indicara que es un set
print(my_set) #al ejecutarlo nos mostrara el set en cualquier orden

print(my_set.add('java')) #add:incluye una palabra o numero en cualquier orden
print(my_set)

print(my_set.add('agua')) #en este caso al ya estar la palabra agua el set quedara igual
print(my_set)

my_set_0 = {'hola','agua','python'}

my_set.difference_update(my_set_0)
print(my_set)