my_dict = {'a','b'}
print(type(my_dict)) #indicara que es un set ya que no es la estrucutura correcta

my_dict = {'Nombre':'Aylin','Color':'Azul','Idioma':'Español'}
print(type(my_dict)) #con la estrucutura correta indicara que es un diccionario

print(my_dict['Idioma']) #de esta forma se ejecutara lo que piden entre los [
    
print(my_dict.keys()) #keys:mostrara todas las llaves
print(my_dict.values()) #values:mostrara todos los valores

#ya sea que se cambie el diccionario a lista,tupla o set solo se mostraran las llaves:

my_dict = list(my_dict)
print(my_dict)

my_dict = tuple(my_dict)
print(my_dict)

my_dict = set(my_dict)
print(my_dict)
