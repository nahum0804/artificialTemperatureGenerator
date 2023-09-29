#Get data of the temperature sensor range


import random
import time #For generate random numbers

#Global Variables
celciusCounter = 0
fareheitCounter = 0

minorCelcius = 0
majorCelcius = 0

minorFahrenheit = 0
majorFahrenheit = 0

lastDate = ""
lastHour = ""

# Read File
def readData():
    with open("/home/nahum/Escritorio/Code/Python/TEC/getTime.py/data.txt", "r") as f:
        data = f.read()
    return data

# Get the data of the temperature sensor
def getEachData():
    global majorCelcius, minorCelcius, majorFahrenheit, minorFahrenheit, celciusCounter, fareheitCounter, lastDate, lastHour

    cantidadDatosGetted = 0;
    fareheitCounter = 0;
    celciusCounter = 0;

    data = readData()
    data = data.split("\n")
    
    for i in range(len(data)):
        arrayIndividual = data[i].split(",")

        celcius = int(arrayIndividual[0].split()[0])
        fahrenheit = int(arrayIndividual[1].split()[0])
        date = arrayIndividual[2]
        hour = arrayIndividual[3]


        if(minorCelcius == 0 and minorFahrenheit == 0):
            minorCelcius = celcius
            minorFahrenheit = fahrenheit

        # Get the major and minor temperature of the data
        if(celcius > majorCelcius):
            majorCelcius = celcius
        
        if(celcius < minorCelcius):
            minorCelcius = celcius

        if(fahrenheit > majorFahrenheit):
            majorFahrenheit = fahrenheit
        
        if(fahrenheit < minorFahrenheit):
            minorFahrenheit = fahrenheit


        print("Celcius: ", celcius)
        print("Fahrenheit: ", fahrenheit)
        print("Date: ", date)
        print("Hour: ", hour)

        # Get the last date and hour
        lastDate = date
        lastHour = hour

        # In this part we need build a dictionary with the data and upload in the firebase
        #
        #
        #
        #
        #


        fareheitCounter += fahrenheit
        celciusCounter += celcius
        cantidadDatosGetted += 1

    # Generat a promedio of the data
    fareheitCounter = fareheitCounter / cantidadDatosGetted
    celciusCounter = celciusCounter / cantidadDatosGetted

    fareheitCounter = round(fareheitCounter, 2)
    celciusCounter = round(celciusCounter, 2)

    print("Promedio de Fahrenheit: ", fareheitCounter)
    print("Promedio de Celcius: ", celciusCounter)
    

    print("Mayor Fahrenheit: ", majorFahrenheit)
    print("Menor Fahrenheit: ", minorFahrenheit)
    print("Mayor Celcius: ", majorCelcius)
    print("Menor Celcius: ", minorCelcius)


def generateMoreData():
    #Generate most data in base of the data getted and the promedio
    print("Generando mas datos...")

    global majorCelcius, minorCelcius, majorFahrenheit, minorFahrenheit, lastDate, lastHour
    
    for i in range(1296000):
        newCelcius = random.uniform(minorCelcius, majorCelcius)
        newFahrenheit = random.uniform(minorFahrenheit, majorFahrenheit)

        newCelcius = int(round(newCelcius, 2))
        newFahrenheit = int(round(newFahrenheit, 2))

        lastHour = lastHour.split(":")
        for i in range(len(lastHour)):
            lastHour[i] = int(lastHour[i])
        
        # Establecer difeereencia según la hora
        if((lastHour[0] >= 10) and (lastHour[0] <= 14)):
            newCelcius = random.uniform(minorCelcius + 2, majorCelcius + 2)
            newFahrenheit = (celciusCounter * 1.8) + 32

            newCelcius = int(round(newCelcius, 2))
            newFahrenheit = int(round(newFahrenheit, 2))
        elif((lastHour[0] >= 19) and (lastHour[0] <= 0)):
            newCelcius = random.uniform(minorCelcius - 2, majorCelcius - 2)
            newFahrenheit = (celciusCounter * 1.8) + 32

            newCelcius = int(round(newCelcius, 2))
            newFahrenheit = int(round(newFahrenheit, 2))
        elif((lastHour[0] >= 0) and (lastHour[0] <= 5)):
            newCelcius = random.uniform(minorCelcius - 3, majorCelcius - 3)
            newFahrenheit = (celciusCounter * 1.8) + 32

            newCelcius = int(round(newCelcius, 2))
            newFahrenheit = int(round(newFahrenheit, 2))


        if(lastHour[2] == 59):
            if(lastHour[1] == 59):
                if(lastHour[0] == 24):
                    lastHour[0] = 00
                    lastHour[1] = 00
                    lastHour[2] = 00
                    #If this, add one day
                    print(lastDate)
                    lastDateS = lastDate.split("-")
                    lastDateS[2] = int(lastDateS[2])
                    lastDateS[1] = int(lastDateS[1])
                    lastDateS[0] = int(lastDateS[0]) + 1

                    print(lastDateS[0])
                    print(lastDateS[1])
                    print(lastDateS[2])

                    if(lastDateS[1] == 1 or lastDateS[1] == 3 or lastDateS[1] == 5 or lastDateS[1] == 7 or lastDateS[1] == 8 or lastDateS[1] == 10):
                        if(lastDateS[0] == 31):
                            lastDateS[1] += 1 
                            lastDateS[0] = 1
                            lastDate = str(lastDateS[0] + 1) + "-" + str(lastDateS[1]) + "-" + str(lastDateS[2])
                    elif(lastDateS[1] == 12):
                        if(lastDateS[0] == 31):
                            lastDateS[1] = 1  
                            lastDateS[0] = 1
                            lastDateS[2] += 1
                            lastDate = str(lastDateS[0]) + "-" + str(lastDateS[1]) + "-" + str(lastDateS[2])
                    elif(lastDateS[1] == 2):
                        if(lastDateS[0] == 28):
                            lastDateS[1] += 1 
                            lastDateS[0] = 0
                            lastDate = str(lastDateS[0]) + "-" + str(lastDateS[1]) + "-" + str(lastDateS[2])
                    elif(lastDateS[1] == 4 or lastDateS[1] == 6 or lastDateS[1] == 9 or lastDateS[1] == 11):
                        if(lastDateS[0] == 30):
                            lastDateS[1] += 1 
                            lastDateS[0] = 1
                            lastDate = str(lastDateS[0]) + "-" + str(lastDateS[1]) + "-" + str(lastDateS[2])
                    else:
                        lastDate = str(lastDateS[0]) + "-" + str(lastDateS[1]) + "-" + str(lastDateS[2]) 

                    lastDate = str(lastDateS[0]) + "-" + str(lastDateS[1]) + "-" + str(lastDateS[2])

                else:
                    lastHour[0] += 1
                    lastHour[1] = 00
                    lastHour[2] = 00
            else:
                lastHour[1] += 1
                lastHour[2] = 00
        else:
            lastHour[2] += 1

        lastHour = str(lastHour[0]) + ":" + str(lastHour[1]) + ":" + str(lastHour[2])
        


        print("Celcius: ", newCelcius)
        print("Fahrenheit: ", newFahrenheit)
        print("Date: ", lastDate)
        print("Hour: ", lastHour)


        dataToSend = str(newCelcius) + ", " + str(newFahrenheit) + ", " + lastDate + ", " + lastHour
        
        
        # Upload the data in the firebase




getEachData()
print("\n")
generateMoreData()
