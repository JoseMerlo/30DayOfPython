#Variables en Python
from os import PRIO_USER


first_name = 'Jose'
last_name = 'Merlo'
pais = 'Honduras'
edad = 25
skills = ['HTML', 'CSS', 'JS', 'PYTHON']

print('Hola Mundo') #El texto hola mundo es un argumento
print(len('Hello World'))

#Tipos de datos
print(type('Jose'))
print(type(first_name))
print(type(10))
print(type(1 + 1j))
print(type(True))
print(type([1,2,3,4]))
print(type({'name': 'jose', 'age': '25',}))

# int a float 
num_int  =  10 
print ( 'num_int' , num_int )          # 10 
num_float  =  float ( num_int )
print ( 'num_float:' , num_float )    # 10.0 

# float a int 
gravedad  =  9.81 
print ( int ( gravedad ))              # 9 

# int a str 
num_int  =  10 
print ( num_int )                   # 10 
num_str  = str ( num_int )
print ( num_str )                   # '10' 

# str a int o float 
num_str  =  '10.6' 
print ( 'num_int' , int ( num_str ))       # 10 
print ( 'num_float' , float ( num_str ))   # 10.6 

# str to list 
first_name  =  'Asabeneh' 
print ( first_name )                # 'Asabeneh' 
first_name_to_list  =  lista (first_name )
print ( first_name_to_list )  