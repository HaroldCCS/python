#variable
"""
edad = 24"""

#condiciones y operador logico
"""
if edad > 20 and edad < 25:
    print ('si cumple las condiciones')
else:
    print ('no cumple las condiciones')
"""

#while
"""
numero = 1
while (numero < 5):
    print("el numero es ",numero)
    numero = numero + 1
"""

#funcion
"""
def comer(variable_1 = 'comida1' , variable_2 = 'comida 2'):
    print ('Hora de comer :D')
    print (variable_1, ' con ', variable_2)

comer('pasta', 'leche')
"""

#tupla o arregle
"""
tupla =('dato 1', 'dato 2', 'dato 3 ')
print (tupla[0])
"""

#recorrer tupla con while
"""
indice = 0
while indice < len (tupla):
    print (tupla[indice])
    indice = indice + 1 
"""
#recorrer tupla con for
"""
for recorre in tupla:
    print (recorre)
"""

#guardar tupla en otra tupla con rangos
"""
tupla = (12, 32, 43, 34, 65, 65)
tupla2 = tupla[0:5]
print (tupla2)
"""
#manejo de cadenas de texto
"""
nombre = "Harold Stiven Camargo Castellanos"
print (nombre[:6]) #inicia desde el 0 y termina en el 6
print (nombre[6:]) # inicia despues del 6
"""

#la lista y las tuplas con arerglos, pero las listas se pueden modificar: lista []  tupla ()
"""
lista = ['Angela', 'Pedro', 65, 74]

if 65 in lista:
    print('Si esta el 65')
else:
    print ('No esta el numero')

print (lista[-1]) # trae ultimo elemento de la lista 
"""

#Diccionario, cuando le asiganos nombre a las variables dentro del array   {  }
"""
diccionario = {'Harold':18, 'Samir':26, 'mama':58}

print (diccionario['Harold'])

print (len(diccionario)) #len para saber tamaño de un array
"""
#help (tupla)   para pedir ayuda sobre las funciones de un elemento
#type (x)  para saber el typo de dato (boleano, int, string etc)
#str (variable) para convertir una variable numerica a string
#dir (tupla) muestra funciones de la tupla

























