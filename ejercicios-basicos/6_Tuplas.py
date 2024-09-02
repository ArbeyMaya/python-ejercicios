### TUPLES ###

# En Python, una tupla es una colección ordenada e inmutable de elementos. Al igual que las listas, las tuplas pueden contener elementos 
# de cualquier tipo de datos (enteros, cadenas, listas, otras tuplas, etc.). Sin embargo, a diferencia de las listas, 
# las tuplas no se pueden modificar después de su creación, es decir, son inmutables.

my_tuple = ()
my_other_tuple = ()

my_tuple = (35, 1.72, "Arbey", "Arbey", "Maya", "Satiaca")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_other_tuple)
print(type(my_other_tuple))

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count("Arbey")) #2, muestra las veces que esta este valor en la tupla
print(my_tuple.index("Maya")) #4, muestra en que parte de la tupla se encuentra ubicado
print(my_tuple.index(35)) #0

#CONCATENACION
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))