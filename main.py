import numpy as np
import random as rd

def fibonacci(num_fibonacci):
    listFibonacci = [0, 1]
    for i in range(num_fibonacci):
        listFibonacci.append((listFibonacci[i] + listFibonacci[i+1]))
    return listFibonacci

def generateRamdonList():
    listRandom = []
    for i in range(int(rd.random() * 1001)):
        listRandom.append(int(rd.random() * 100))
    return listRandom

def sumList(listData):
    sum = 0
    print(listData)
    for i in range(len(listData)):
        sum += listData[i]
    return sum

def clave_valor():
    edad = {
        "Juan" : 19,
        "David": 20,
        "Mauricio" : 17,
        "Shirley" : 17,
        "Yessica" : 20
    }

    for nombre in edad:
        print("Nombre {} edad {}".format(nombre, edad[nombre]))

def input_name():
    name = input("Cual es tu nombre: ")
    print("Bienvenido {}".format(name))

def pay_hours():
    Hours = input("Enter Hours: ")
    Rate = input("Enter Rate: ")
    iHours = int(Hours)
    iRate = float(Rate)
    print("Pay: {}".format(iHours * iRate))

pay_hours()
# inputName()
# clave_valor()
#listData = np.array(generateRamdonList())
#print("La suma de todos los valores es {}".format(sumList(listData)))
#print("La media de esta lista es {:1f}".format(listData.mean()))
#print("El maximo valor de esta lista es {}".format(listData.max()))
#print("El valor minimo es {}".format(listData.min()))
#print("La logintud de esta lista es {}".format(len(listData)))



#listToSum = [1, 4, 3, 2, 4, 2, 5]
#print(sumList(listToSum))

#num_sec = 100
#print(fibonacci(num_sec))
#nparray = np.array(fibonacci(num_sec))
#print("la media de esta secuencia de fibonacci es {:2f}".format(nparray.mean()))