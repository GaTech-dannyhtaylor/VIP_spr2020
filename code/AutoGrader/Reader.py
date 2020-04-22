import os
import csv
from os import listdir

from GTPoint import *
from GTSign import *
from Route import *
from UserPoint import *
from UserSign import *
from groundTruthWeight import *

class Reader:

	def __init__(self):
		pass

	# methods for reading in a GT route
	def createPointList(self, signPath):
	    # Read in points from SignPoints.txt
	    signPointsPath= signPath + "/SignPoints.txt"
	    signPointsFile = open(signPointsPath, "r")
	    signPointsList = signPointsFile.readlines()

	       #Removing the line return character
	    for i in range(len(signPointsList)):
	        signPointsList[i] = signPointsList[i].replace('\n',"")
	    # print(signPointsList)

	    pointList = []
	    for i in range(1, len(signPointsList)):
	        # print('We are on point number: {}'.format(i))
	        row = signPointsList[i].split(" ")
	        id = float(row[0])
	        easting = float(row[1])
	        northing = float(row[2])
	        altitude = float(row[3])
	        retro = float(row[4])
	        angle = float(row[5])
	        distance = float(row[6])
	        utc = float(row[7])
	        long = float(row[8])
	        lat = float(row[9])
	        signPoint = GTPoint(id, easting, northing, altitude, retro, angle, distance, utc, long, lat)
	        pointList.append(signPoint)

	    # Create values for all GT points in point list

	    return pointList

	def createSign(self, signPath):

	    # Get the sign properties
	    signPropertiesPath = signPath + "/SignProperties.txt"
	    signPropertiesFile = open(signPropertiesPath, "r")
	    signPropertiesList = signPropertiesFile.readlines()

	    #Removing the line return character
	    for i in range(len(signPropertiesList)):
	        signPropertiesList[i] = signPropertiesList[i].replace('\n',"")
	    # print(signPropertiesList)

	    # Get Sign Properties
	    signID = signPropertiesList[0].split(":", 1)[1]
	    signType = signPropertiesList[1].split(":", 1)[1]
	    signPic = signPropertiesList[2].split(":", 1)[1]

	    pointList = self.createPointList(signPath)
	    signDescription = GTSign(signID, signType, signPic, pointList)

	    signDescription = groundTruthWeight(signDescription) # Assign gtpoint values here!!!

	    return signDescription

	def createSignList(self, path, totalSigns):
	    signList = []
	    for i in range(totalSigns):
	        signPath = path + "/Sign " + str(i)
	        signList.append(self.createSign(signPath))
	        # print("We are on sign number: {}".format(i))
	    return signList

	def createRoute(self, path):
	    routePropertiesName = path+"/RouteProperties.txt"
	    # Access Route Properties
	    routeProperties = open(routePropertiesName, "r")
	    routePropertiesList = routeProperties.readlines()
	    
	    #Removing the line return character
	    for i in range(len(routePropertiesList)):
	        routePropertiesList[i] = routePropertiesList[i].replace('\n',"")


	    roadWay = routePropertiesList[0].split(": ", 1)[1]
	    # print(roadWay)

	    year = int(routePropertiesList[1].split(": ", 1)[1])
	    # print(year)

	    startingGps = tuple(map(float, routePropertiesList[2].split(':')[1].split(',')))
	    # print(startingGps)

	    endingGps = tuple(map(float, routePropertiesList[3].split(':')[1].split(',')))
	    # print(endingGps)

	    startingUTM = tuple(map(float, routePropertiesList[4].split(':')[1].split(',')))

	    endingUTM = tuple(map(float, routePropertiesList[5].split(':')[1].split(',')))

	    startingPic = float(routePropertiesList[6].split(":", 1)[1])

	    endingPic = float(routePropertiesList[7].split(":", 1)[1])

	    distance = 0 #float(routePropertiesList[8].split(": ", 1)[1].split("\n",1)[0])

	    totalSigns = int(routePropertiesList[9].split(":", 1)[1])

	    warningSigns = int(routePropertiesList[10].split(":", 1)[1])

	    regulatorySigns = int(routePropertiesList[11].split(":", 1)[1])

	    guidingSigns = int(routePropertiesList[12].split(":", 1)[1])

	    constructionSigns = int(routePropertiesList[13].split(":", 1)[1])

	    otherSigns = int(routePropertiesList[14].split(":", 1)[1])

	    signList = self.createSignList(path, totalSigns)
	    route = Route(signList, roadWay, year, startingGps, endingGps, startingUTM, endingUTM, startingPic, endingPic, distance, totalSigns, warningSigns, regulatorySigns, guidingSigns, constructionSigns, otherSigns)
	    return route

    # method for reading in user output
	def collectUserSigns(self,path):
	    count = 0
	    Dict = {}
	    Dict[0] = []

	    with open(path, newline = '') as csvfile:
	        reader = csv.reader(csvfile, delimiter = ',')
	        next(reader, None)
	        for row in reader:
	            # print(row)
	            signID = int(row[0])
	            if signID == count:
	                Dict[count].append(UserPoint(int(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10])))
	            else:
	                count = count + 1
	                Dict[count] = []
	                Dict[count].append(UserPoint(int(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10])))

	    finalList = []
	    for key, value in Dict.items():
	        finalList.append(UserSign(key, value))

	    return finalList