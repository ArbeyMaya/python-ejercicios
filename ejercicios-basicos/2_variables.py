#Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = "5"
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
    #Para concatenar se separa por una ,
print( "El valor de esta variable es: ", my_int_variable )


#ALGUNAS FUNCIONES DEL SISTEMA

    #len: cuenta los caracteres que tenga la variable
print(len(my_string_variable)) #Esta variable cuenta con 18 caracteres

    #variables en una sola linea
nombre, apellido, edad, telefono = "Vilmar", "Maya", 23, 3155566304
print("Mi nombre es: ", nombre, "Mi apellido es: ", apellido, "Mi numero de telefono es: ", telefono, "Y mi edad es: ", edad)

    #Inpunts
nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")

print("Hola, Bienbenido ",nombre, apellido)