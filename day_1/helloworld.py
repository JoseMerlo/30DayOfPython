
# Día 1 - 30DaysOfPython Challenge 



#String
from pickle import TRUE


print('Asabeneh')
print('Honduras')
print('Me gusta Python')

#Boolean
luz = True
luz2 = False
print(luz)


#Lista
[0,1,2,3,4,5] #Lista de numeros
['Banana','Orange','Mango','Color'] #Lista de cadenas (frutas, color)
['Finlandia','Honduras','Suecia','Noruega'] # lista cadenas (paises)
['Pera', 10, False, 9.10] # lista cadena, entero, booleano, flotante


#Diccionario
#Un objeto de diccionario de Python es una colección desordenada de datos en un formato de par de valores clave.

{
    'first_name': 'Jose',
    'last_name': 'Francisco',
    'age': 25,
    'is_married':True,
    'skills':['JS','HTML', 'Python', 'CSS'],
    
}

#Tupla
#Una tupla es una colección ordenada de diferentes tipos de datos como una lista, pero las tuplas no se pueden modificar una vez que se crean. Son inmutables.
('Jose', 'Merlo', 'Brook', 'Abraham', 'Olimpia')#Nombres


#Set (Colecciones)
#Un conjunto es una colección de tipos de datos similar a una lista y una tupla. A diferencia de list y tuple, set no es una colección ordenada de elementos. Al igual que en Matemáticas, la configuración en Python almacena solo elementos únicos.
{2, 3, 5, 6}
{2.14, 9.81, 2.7}


#Tipos de datos
print(2+3) #suma
print(3-1) #resta
print(2*3) #multiplicacion
print(3/1) #division
print(3**2) #exponecial
print(3%2) #modulo
print(3//2) #operador de division de planta

#Comprobando tipos de datos
print(type(10)) #Int
print(type(3.14)) #Float
print(type(1+3j)) #Numero complejo
print(type("Hola")) #Cadena
print(type([1,2,3])) #Lista
print(type({'Nombre': 'Jose'})) #Diccionario
print(type({9,8, 3.14, 2.7})) #Set
print(type((9,8, 3.14, 2.7))) #Tupla