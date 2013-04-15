#generates random .aut files
from random import *
import string
import os

n = 100;

for i in range(n):
    random = Random()
    random.seed(i)

    xLow = random.randint(-50,50)
    xHigh = random.randint(-50,50)
    if(xLow > xHigh):
        tmp = xLow
        xLow = xHigh
        xHigh = tmp

    yLow = random.randint(-50,50)
    yHigh = random.randint(-50,50)
    if(yLow > yHigh):
        tmp = yLow
        yLow = yHigh
        yHigh = tmp

    f = open("test/input/test" + str(i) + ".aut", "w")

    f.write("Xrange " + str(xLow) + " " + str(xHigh) + ";\n")
    f.write("Yrange " + str(yLow) + " " + str(yHigh) + ";\n")

    f.write('Name "Generated by Ryan mwahaha";\n')

    rd = random.randint(0,255)
    gd = random.randint(0,255)
    bd = random.randint(0,255) 
    ra = random.randint(0,255) 
    ga = random.randint(0,255) 
    ba = random.randint(0,255) 
         
    f.write("Colors (" + str(rd) + ", " + str(gd) + ", " + str(bd) + "), (" + str(ra) + ", " + str(ga) + ", " + str(ba) + ");\n")
    f.write("Chars " + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) + 
                       ", " + 
                       random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                       + ";\n")


    f.write("Initial {\n")
    firstX = True
    yList = range(yLow, yHigh+1)
    random.shuffle(yList)
    for y in yList:
        if(random.choice([True,False])):
            f.write("Y = " + str(y) + " : ")
            xList = range(xLow, xHigh+1)
            random.shuffle(xList)
            for x in xList: 
                    if(firstX):
                        f.write(str(x))
                        firstX = False
                    elif(random.choice([True,False])):
                        f.write("," + str(x))
            f.write(";\n")
            firstX = True
    f.write("};\n")

