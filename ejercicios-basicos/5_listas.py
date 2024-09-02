### LIST ###


#  En Python, una lista es una estructura de datos que permite almacenar múltiples elementos en una sola variable. 
# Los elementos de una lista pueden ser de diferentes tipos (números, cadenas, booleanos, incluso otras listas). 
# Las listas en Python son mutables, lo que significa que puedes modificar sus elementos después de haberlas creado 
# (añadir, eliminar o cambiar elementos).

#Lista vacia
my_list = list()
my_other_list = []

#Longitud de una lista "len"
print(len(my_list))

#Asignado numeros a la lista
my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [23, 1.72, "Arbey", "Maya"]

print(my_list)
print(len(my_list))

print(my_other_list)
print(len(my_other_list))

#clase "type"
print(type(my_list))
print(type(my_other_list))


### ACCESO A ELEMENTOS Y BUSQUEDA ###
print(my_other_list[0]) #23
print(my_other_list[1]) #1.72

#imprime el ultimo valor de la lista "-1"
print(my_other_list[-1]) #Maya
print(my_other_list[-4]) #23

#contar cuántas veces aparece un elemento específico en una lista. ".count()"
print(my_list.count(30))#2

#para encontrar el índice (posición) de un elemento específico en una lista. ".index()"
print(my_other_list.index(23)) #Posicion 0

#desempaquetado 
edad, estatura, nombre, apellido = my_other_list
print(edad) #23
print(apellido) #Maya

### CONCATENACION, INSERCION, ACTUALIZACION Y ELIMINACION ###
print(my_list + my_other_list)

### CREACION ###
#le añade un nuevo elemento al final ".append"
my_other_list.append("Satiaca")
print(my_other_list)

# insertar un elemento en una posición específica. ".insert()"
my_other_list.insert(1, "Rojo")
print(my_other_list)

#cambia el valor del elemento existente y lo reemplaza.
my_other_list[1] = "Azul"
print(my_other_list)

#elimina el elemento con el mismo nombre o valor
my_other_list.remove("Azul")
print (my_other_list)

my_list.remove(30)
print(my_list)

#Elimina el ultimo elemento ".pop" ".pop() = muestra el elemento eliminado"
print(my_list.pop())
print(my_list)

#Elimina el elemento que esta en la posicion 2
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

print("separador")
#Igualmente elimina el elemento mecionado
del my_list[2]
print(my_list)

### OPERACIONES CON LISTAS ###
print("Operaciones con listas")

# Esta línea crea una nueva lista llamada my_new_list que es una copia exacta de la lista my_list. 
# Esto significa que cualquier cambio que se realice en una lista no afectará a la otra.
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

#Imprime la lista de manera desendente
my_new_list.reverse()
print(my_new_list)

#Imprime de menor a mayor
my_new_list.sort()
print(my_new_list)

### SUBLISTAS ###
#Es una sintaxis para especificar un rango de índices
print(my_new_list[1:3])

### CAMBIO DE TIPO ###
my_list = "Hola Python"
print(my_list)
print(type(my_list))
