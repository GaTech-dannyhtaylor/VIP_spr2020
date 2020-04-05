import os
from os import listdir

from GTPoint import *
from GTSign import *
from Route import *
def createPointList(signPointsList):
    pointList = []
    for i in range(1, len(signPointsList)):
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
        lat = float(row[9].split("\n", 1)[0])
        signPoint = GTPoint(id, easting, northing, altitude, retro, angle, distance, utc, long, lat)
        pointList.append(signPoint)
    return pointList

def createSign(signPropertiesList):
    signID = signPropertiesList[0].split(": ", 1)[1].split("\n", 1)[0]
    signType = signPropertiesList[1].split(": ", 1)[1].split("\n", 1)[0]
    signPic = signPropertiesList[2].split(": ", 1)[1].split("\n", 1)[0]
    signPointsName = path + "/Sign 0/SignPoints0.txt"
    signPoints = open(signPointsName, "r")
    signPointsList = signPoints.readlines()
    pointList = createPointList(signPointsList)
    signDescription = GTSign(signID, signType, signPic, pointList)
    return signDescription


def createSignList(path, totalSigns):
    signList = []
    for i in range(totalSigns):
        signPropertiesName = path + "/Sign " + str(i) + "/SignProperties.txt"
        signProperties = open(signPropertiesName, "r")
        signPropertiesList = signProperties.readlines()
        signList.append(createSign(signPropertiesList))
    return signList
def createRoute(path):
    routePropertiesName = path+"/RouteProperties.txt"
    # Access Route Properties
    routeProperties = open(routePropertiesName, "r")
    routePropertiesList = routeProperties.readlines()
    roadWay = routePropertiesList[0].split(": ", 1)[1].split("\n",1)[0]
    year = int(routePropertiesList[1].split(": ", 1)[1].split("\n",1)[0])
    startingGps = routePropertiesList[2].split(": ", 1)[1].split("\n",1)[0]
    endingGps = routePropertiesList[3].split(": ", 1)[1].split("\n",1)[0]
    startingUTM = routePropertiesList[4].split(": ", 1)[1].split("\n",1)[0]
    endingUTM = routePropertiesList[5].split(": ", 1)[1].split("\n",1)[0]
    startingPic = float(routePropertiesList[6].split(": ", 1)[1].split("\n",1)[0])
    endingPic = float(routePropertiesList[7].split(": ", 1)[1].split("\n",1)[0])
    distance = 0 #float(routePropertiesList[8].split(": ", 1)[1].split("\n",1)[0])
    totalSigns = int(routePropertiesList[9].split(": ", 1)[1].split("\n",1)[0])
    warningSigns = int(routePropertiesList[10].split(": ", 1)[1].split("\n",1)[0])
    regulatorySigns = int(routePropertiesList[11].split(": ", 1)[1].split("\n",1)[0])
    guidingSigns = int(routePropertiesList[12].split(": ", 1)[1].split("\n",1)[0])
    constructionSigns = int(routePropertiesList[13].split(": ", 1)[1].split("\n",1)[0])
    otherSigns = int(routePropertiesList[14].split(": ", 1)[1].split("\n",1)[0])
    signList = createSignList(path, totalSigns)
    route = Route(signList, roadWay, year, startingGps, endingGps, startingUTM, endingUTM, startingPic, endingPic, distance, totalSigns, warningSigns, regulatorySigns, guidingSigns, constructionSigns, otherSigns)
    return route

# Given Path
path = "2016"