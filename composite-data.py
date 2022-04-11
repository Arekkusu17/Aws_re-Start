import csv
import copy

myVehicle={
    "vin":"<empty>",
    "make":"<empty>",
    "model":"<empty>",
    "year":0,
    "range":0,
    "topSpeed":0,
    "zeroSixty":0.0,
    "mileage":0
}

for key, value in myVehicle.items():
    print(f"{key}:{value}")
    
myInventoryList=[]

#mantiene abierto el archivo csv para leer sus datos, cuando se salga del bloque with, se cierra el archivo

with open('car_fleet.csv') as csvFile:
    csvReader= csv.reader(csvFile, delimiter=",")
    linecount=0;
    for row in csvReader:
        #la primera linea trae escrito el orden de las key en columnas separadas por ","
        if linecount==0:
            print(f'columns are: {",".join(row)}')
            linecount+=1
        else:
            #se imprime cada línea las respectivas values con sus key a modo de observar
            print(f'vin:{row[0]} make:{row[1]} model:{row[2]} year:{row[3]} range:{row[4]} topSpeed:{row[5]} zeroSixty:{row[6]} mileage:{row[7]}')
            #copia el formato que tiene myVehicle en el sentido de ser un diccionario, es un "template"
            currentVehicle= copy.deepcopy(myVehicle)
            currentVehicle["vin"]=row[0]
            currentVehicle["make"]=row[1]
            currentVehicle["model"]=row[2]
            currentVehicle["year"]=row[3]
            currentVehicle["range"]=row[4]
            currentVehicle["topSpeed"]=row[5]
            currentVehicle["zeroSixty"]=row[6]
            currentVehicle["mileage"]=row[7]
            #se agrega el vehiculo al inventario de vehiculos
            myInventoryList.append(currentVehicle)
            linecount+=1
    #nos dice cuantas lineas se procesaron en total
    print(f'Proccesed {linecount} lines.')
        
        
#con este loop, mostramos los items al interior del inventario 
for myCarProperties in myInventoryList:
    for key,value in myCarProperties.items():
        #imprime las key y los value
        print(f'{key} : {value}')
    # separa cada vehiculo
    print("----")
