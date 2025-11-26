my_list = ['Python','7',True]

print(type(my_list))
print(my_list[1]) #empieza a contar desde el 0
print(my_list[-1]) #empieza al revez contando desde el 1

#Funciones para listas

my_list.append('hola') #append:inclye una nueva palabra o numero que quieras agregar al final
print(my_list)

my_list.insert(3,'7') #insert:inclye una nueva palabra o numero en el orden que escojas
print(my_list)

my_list.remove('hola') #remove:remueva una palabra o numero que le menciones
print(my_list)

my_list.pop(2) #pop:remueve una palabra o numero al decir su posición
print(my_list)

print(my_list.pop(2)) #de esta forma te menciona la palabra que eliminaste anteriormente con pop

print(my_list)
print(my_list.count('7')) #de esta forma se cuenta cuant veces esta ese termino en la lista

my_list.reverse()
print(my_list)

my_list.clear()
print(my_list)
