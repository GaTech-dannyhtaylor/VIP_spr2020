import sys

from groundTruthWeight import *
from setIOU import *
from Point import *
from UserPoint import *
from GTPoint import *
from Sign import *
from UserSign import *
from GTSign import *


def makePointList(pointTXT):
    # Can run through command line: python makePointList.py <space separated arguments>
        # No string quotations needed for string parameters
        # /Users/Gabrielle/School/VIPLiDAR/2018/Route2018/Sign1/SignPoints.txt
            # file is from Danny script that retains metadata, not from CloudCompare

    file = open(pointTXT, "r")
    file.readline()

    pointList = []

    currRow = file.readline()
    while True:
        # following data assignment is from Danny script that retains metadata, not from CloudCompare
        data = currRow.split(" ")
        pointID = int(data[0])
        east = float(data[1])
        north = float(data[2])
        alt = float(data[3])
        retro = float(data[4])
        angle = float(data[5])
        distance = float(data[6])
        utc = float(data[7])
        longi = float(data[8])
        lat = float(data[9])

        point = GTPoint(pointID, east, north, alt, retro, angle, distance, utc, longi, lat)
        pointList.append(point)

        currRow = file.readline()
        if not currRow:
            break

    file.close()

    GTsign = GTSign(1, "R", 1682, pointList)

    groundTruthWeight(GTsign)

    #Testing purpose print statements:
    totalValue = 0
    for point in GTsign.point_list:
        print(f'Point ID {point.point_id} of easting {point.easting} of value {point.value}.')
        totalValue += point.value
    print(totalValue)     # check total of normalized point values is 1



def makeUserAndGTSign(userTXT, gtTXT):
    # Can run through command line: python makePointList.py <space separated arguments>
        # No string quotations needed for string parameters
        # /Users/Gabrielle/School/VIPLiDAR/2018/userSign1.txt
        # /Users/Gabrielle/School/VIPLiDAR/2018/gtSign1.txt
            # files are metadata from CloudCompare

    file = open(userTXT, "r")
    file.readline()

    userPointList = []

    currRow = file.readline()
    while True:
        # following data assignment is from CloudCompare
        data = currRow.split(" ")
        east = float(data[0])
        north = float(data[1])
        alt = float(data[2])
        pointID = int(float(data[3]))
        retro = float(data[4])
        angle = float(data[5])
        distance = float(data[6])
        utc = float(data[7])
        longi = float(data[8])
        lat = float(data[9])


        point = UserPoint(pointID, east, north, alt, retro, angle, distance, utc, longi, lat)
        userPointList.append(point)

        currRow = file.readline()
        if not currRow:
            break

    file.close()

    userSign = UserSign(1, userPointList)


    file2 = open(gtTXT, "r")
    file2.readline()

    gtPointList = []

    currRow = file2.readline()
    while True:
        # following data assignment is from CloudCompare
        data = currRow.split(" ")
        east = float(data[0])
        north = float(data[1])
        alt = float(data[2])
        pointID = int(float(data[3]))
        retro = float(data[4])
        angle = float(data[5])
        distance = float(data[6])
        utc = float(data[7])
        longi = float(data[8])
        lat = float(data[9])


        point = GTPoint(pointID, east, north, alt, retro, angle, distance, utc, longi, lat)
        gtPointList.append(point)

        currRow = file2.readline()
        if not currRow:
            break

    file2.close()

    gtSign = GTSign(1, "R", 1682, gtPointList)

    setIOU(gtSign, userSign)

    #Testing purpose print statements:
    for point in userSign.point_list:
        print(f'Point ID {point.point_id} of easting {point.easting} of type {point.type}.')





if __name__ == '__main__':
    # Map command line arguments to function arguments.
    # makePointList(*sys.argv[1:])
    makeUserAndGTSign(*sys.argv[1:])



















