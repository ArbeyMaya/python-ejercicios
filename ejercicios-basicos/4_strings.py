### STRINGS ###

my_string = "my string"
my_oyher_string = "Mi otro string"

print(len(my_string))
print(len(my_oyher_string))

print((my_oyher_string + " " + my_string))

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion "
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado "
print(my_scape_string)

my_scape_string = "\\tEste es un string \\n escapado "
print(my_scape_string)

#Formateo
    #se puede modificar
nombre, apellido, edad = "Vilmar", "Arbey", 23
print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))
    #No se puede modificar
print("Mi nombre es %s %s y tengo %d años" %(nombre, apellido, edad))

print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")


#Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

#Division

language_slice = language[1:3]
print(language_slice)

lenguage_slice = language [1:]
print(lenguage_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje
print(language.capitalize()) #Convierte el primer caracter en mayuscula
print(language.upper()) #Convierte todos los caracteres en mayuscula
print(language.count("t")) #Cuenta cuantas t hay en los caracteres
print(language.isnumeric()) #verificar si todos los caracteres en una cadena son numéricos
print("1".isnumeric())
print(language.lower()) #minuscula todos los caracteres
print(language.lower().isupper())
print(language.startswith("Py")) #startswith devuelve True si la cadena comienza con el prefijo especificado y False en caso contrario.
print("Py" == "py")  # No es lo mismo