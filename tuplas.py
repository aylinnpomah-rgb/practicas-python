my_tupla = (3.3, 'hola', 45,)
print(type(my_tupla))

print(my_tupla[2]) #te menciona el termino por la posición que hayas puesto

print(my_tupla.count(45)) #count:cuantas veces esta el termino
print(my_tupla.index(3.3)) #index:nos dice en que posición esta ese termino

#pasar de una tupla a una lista
my_tupla = list(my_tupla)
print(type(my_tupla)) #te dira que ahora es una lista

#pasar de lista a tupla
my_tupla = tuple(my_tupla)
print(type(my_tupla))