"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por la pantalla la paga que le corresponda.
"""

hoursWorked=float(input("¿Cuántas horas ha trabajado?"))
hourlyCost=float(input("¿Cuál es el coste por hora?"))
toPay=hourlyCost*hoursWorked

print(f"Le corresponde {toPay} de paga")



"""
Escribir un programa que lea un entero positivo n, introducido por el usuario y despures muestre enpantalla la suma de todos los numeros desde 1 hasta n
"""
number=int(input("Ingresa un número "))
sum=((number*(number+1))/2)

print (f"La suma desde 1 hasta {number} es {sum}")



"""
Escribir un programa que pida al usuario su peso en Kg, y estatura en metros. Calcule el indice de maca corporal.
Muestre en la pantalla "tu indice de masa corporal es imc donde imc es el indice de masa corporal redondeado con dos decimlaes
"""

weight=float(input("Ingrese su peso en Kilogramos: "))
height=float(input("Ingrese su estatura en metros: "))

imc=((weight)/(height*height))

print (f"Tu índice de masa corporal es {imc} donde {round(imc,2)} es el índice de masa corporal calculado redondeado con dos decimales")


"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la division de "n" entre "m" da un cociente c y un resto r 
donde n y m son numeros introducidos por el usuario y c y r son el cociente y el resto de la division entera respectivamente
"""

n=int(input("Ingrese un número (dividendo) entero: "))
m=int(input("Ingrese un número (divisor) entero: "))

c=int(n/m)
r=n-c*m

print (f"La división entera de {n} entre {m} da un cociente={c} y un resto={r}, donde {n} y {m} son números introducidos por el usuario")



"""
Se requiere solicitar al usuario las ultimas diez calificaciones de su curso de
AWS re/Star 
Luego de esto es necesario mostrar la media de todas estas calificaciones.
Si la media de las notas es mayor que 70 puntos mostrar mensaje
Si la media es inferior a 70, mostrar mensaej
"""
grades=[]

for i in range(0,10):
    grade=float(input("Ingrese cada calificación:"))
    grades.append(grade)
    
average=(sum(grades)/10)

print(f"La media obtenida es {average}")

if(average>70):
    print("FELICIDADES! APROBASTE. :)")
elif(average<70):
    print("RECUERDA ENCENDER LA CÁMARA")
    
"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla, 3 veces en upper
3 veces en lower y 3 veces en title
"""

string=input("Ingrese una palabra: ")
word=string.lower()

for i in range(0,9):
    if i<3:
        print(word.lower())
    elif i<6:
        print(word.upper())
    else:
        print(word.title())
        

"""
Escribir un programa que pida al usuario una palabra y almacene la palabra como la ingreso el usuario,
la palbra en minuscula, la palbra en mayuscula, la palabra capitalizada, y el tamaño de la palabra.
Luego imprimir cada palabra de la lista
"""

""" The user input a word """
word=input("Ingrese una palabra: ")
newList=[]

""" Append the word to a list, using every method needed"""

newList.append(word)
newList.append(word.lower())
newList.append(word.upper())
newList.append(word.title())
newList.append(len(word))

""" Iterate through the list to print each item """
for item in newList:
    print (item)
    
    
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número:
"""

number=int(input("Ingrese un número entero positivo: "))
oddNumbers=[]

for i in range(1,number+1,2):
    oddNumbers.append(str(i));

oddList=",".join(oddNumbers)

print(f"The odd numbers between {1} and {number} are: {oddList}")


"""
Realizar un programa que solicite al usuario el nombre de un país y luego le muestre en la 
consola el la capita de ese pais. Además si el país digitado empieza por "A le debe mostrar el mensaje
"el pais digitado esta seleccionado para donacioens".
Se debe hacer un diccionario
"""

"""
Realizar un programa que solicite al usuario adivinar un numero entre 1 y 10, si el número es
adivinado. si lo adivina mostrtar "CORRECTO" si no "INTENTA DE NUEVO". Opcionalmente que no termine 
hasta q se adivine
"""
import random

target=random.randint(1,10)

print(target)

guess=int(input("¿Adivina el número en que estoy pensando?"))

while guess!=target:
    print("INCORRECTO")
    guess=int(input("Intentalo de nuevo: "))

print("CORRECTO")

"""
Crear un programa que basandose en una lista de numeros entre 1 y 100, solamente imprima los numeros pares.
(apoyraser de x%2==0)
"""

newList=[]
odds=[]
even=[]

for i in range(1,101):
    newList.append(i)

for num in newList:
    if num%2==0:
        even.append(num)
    elif num%2 !=0:
        odds.append(num)



print(f'Los números pares entre 1 y 100 son: {even}')

"""
Realizar un programa que solicite al usuario el nombre de un país y luego le muestre en la 
consola el la capita de ese pais. Además si el país digitado empieza por "A le debe mostrar el mensaje
"el pais digitado esta seleccionado para donacioens".
Se debe hacer un diccionario
"""

countries={"Australia":"Canberra","Barbados":"Bridgetowen","Chile":"Santiago","Japón":"Tokyo","Korea":"Seúl"}

searchForCountry=input("Ingresa un pais para conocer su capital: (Australia, Barbados, Chile, Japón, Korea)")

for el in countries:
    if el==searchForCountry:
        print("La capital es: ")
        print(countries[str(searchForCountry)])



"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba
"salir" que terminará
"""

isEchoeOn=True

while(isEchoeOn!=False):
    toEcho=input("Ingrese una palabra o frase")
    if(toEcho=="salir"):
        isEchoeOn=False
    else:
        print(toEcho)
    

"""
Escribir un programa en que se pregunte al usuario por una frase y una letra, y muestre en la pantalla el 
número de veces que esta esa letra en la frase.
"""

phrase=input("Ingrese una frase: ")
letter=input("Ingrese una letra: ")
count=0

for char in phrase:
    if char==letter:
        count +=1

print(f"La letra {letter} aparece {count} veces en la frase.")
    
    
    
"""
Escribir una función que pida un número entre 1 y 10 y guarde un fichero con el nombre tabla-n.txt la tabla de multiplicar
de ese npumero donde n es el npumero introducido
"""
import os

num=int(input("Ingrese un número del 1 al 10: "))

def tablaMultiplicar(num):
    fileName=f"tabla-{num}.txt"
    file = open(fileName,"w")
    for i in range (1,13):
        file.write(f"{num*i}\n")
    file.close()
    print(f"Se terminó de escribir la tabla del {num}")
    
tablaMultiplicar(num)

"""
Escribir una función que pida un número entre 1 y 10, lea el fichero tabla-n txt con la tabla de multiplicar de n y la muestre en la pantalla.
Si el fichero no existe debe mostrar un mensaje por pantalla de ello.
"""

num=int(input("Ingrese un número del 1 al 10: "))

def tablaMultiplicar2(num):
    fileName=f"tabla-{num}.txt"
    try:
        file=open(fileName,"r")
    except FileNotFoundError:
        print (f"No existe el fichero {fileName}")        
    else: 
        print(file.read())

tablaMultiplicar2(num)
    

"""
Escribir una función que pida un número n y m entre 1 y 10, lea el fichero tabla-n txt con la tabla de multiplicar de n y 
muestre en la pantalla la linea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla de ello.
"""


num=int(input("Ingrese un número del 1 al 10: "))

def tablaMultiplicar3(num):
    fileName=f"tabla-{num}.txt"
    try:
        file=open(fileName,"r")
    except FileNotFoundError:
        print (f"No existe el fichero {fileName}")        
    else:
        m=int(input("Ingrese un número del 1 al 10: "))
        lines=file.readlines()
        try:
            print(lines[m-1])
        except IndexError:
            print(f"La tabla no llega hasta el {m}")

tablaMultiplicar3(num)


"""
Crear un programa que solicite la cantidad de folder a crear y posteriormente cree las carpetas con la nomeclatura
"folder_1","folder_2","folder_3", etc.
"""

import os
import subprocess

flag=True

while flag:
    try:
        num=int(input("Ingrese la cantidad de carpetas a crear (1 a 10 máx): "))
        if (num>=1 and num <=10):
            flag=False
    except:
        print("El número que has digitado es incorrecto, Favor intente nuevamente")
        flag=True
        
        
command="mkdir"
count=1

while count<=num:
    folderName=f"folder_{count}"
    subprocess.run([command,folderName])
    print(command,folderName)
    count +=1
    
print("Carpetas creadas.")