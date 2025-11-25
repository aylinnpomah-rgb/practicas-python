mi_colegio = 'colegio'
mi_casa = 'casa'
mi_mascota = 'mascota'

#print( 'me gusta ' + mi_colegio + '' +  mi_casa + '' +  mi_mascota)
print(f'me gusta { mi_colegio} hoy')

other_string = 'hola'
a,b,c,d = other_string
print(c)
print(f'{a}{b}{c}{d}')

print(mi_colegio.upper()) #upper:pone en mayuscula la frase o palabra que se refiera
print(mi_colegio.capitalize()) #capitalize:pone en mayuscula la primera letra
print(mi_colegio.lower()) #lower:pone todo en minuscula
print(len(mi_colegio)) #len:cuenta la cantidad de caracteres de la palabra que refiere
print(mi_colegio.find('o')) #find:en que posicion esta la letra que se mencione en la palabra
print(mi_colegio.count('o')) #count:cantidad de veces que esta la letra en la palabra que se mencione
