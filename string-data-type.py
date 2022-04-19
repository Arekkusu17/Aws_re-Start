"""
Strings are used often in Python for input and output
"""

myString="This is a string."
print(myString)

print(myString +" is of the data type " + str(type(myString)))


firstString="water"
secondString="fall"
thirdString=firstString+secondString
print(thirdString)


name=input("What is your name? ")
print(name)


color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))



"""
Classes Exercises
"""

"""
Programa que recibe nombre comleto, y printea primero en lower luego en upper y luego en capitalize
"""
name=input("Enter your fullname: ")

print(name.lower())
print(name.upper())
print(name.lower().title())

"""
newName=name.split(" ")
str=[]

for word in newName:
    word=word.lower()
    word=word.capitalize()
    str.append(word)
    
print(" ".join(str))
"""

"""
Escribir un programa que pregunte el nombre del usuario y despues del usuario muestre "nombre tiene n letras"
donndenombre esta en mayusculas y n es el numero de letras
"""

username=input("Ingrese su nombre de usuario: ")
print (len(username))

print(f"El nombre de usuario {username.upper()} tiene {len(username)} carácteres")


"""
Los teléfonos de una empresa tienen el siguiente formato prefijo.num-extension, donde el prfijo
es +34 y la extension tiene dos digitos.
Escriba una programa que pregunte por un número de telefono con este formato y muestre
pro la pantalla el numero de telefono sin el prefijo y la extension
"""


tel=input("ingrese el número de teléfono según formato: ")
numbers=tel.split("-")

print(f"El número de teléfono es {numbers[1]} ")