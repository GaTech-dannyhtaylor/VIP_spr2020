import sys

from groundTruthWeight import *
from GTSign import *
from Sign import *
from GTPoint import *
from Point import *


def makePointList(pointTXT):
    # Can run through command line: python makePointList.py <space separated arguments>
        # No string quotations needed for string parameters
        # /Users/Gabrielle/School/VIPLiDAR/2018/Route2018/Sign1/SignPoints.txt
    file = open(pointTXT, "r")
    file.readline()

    pointList = []

    currRow = file.readline()
    while True:
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

    #Below is print statements to test result of groundTruthWeight result
    totalValue = 0
    for point in GTsign.point_list:
        print(f'Point ID {point.point_id} of easting {point.easting} of value {point.value}.')
        totalValue += point.value
    print(totalValue)
    # check total of normalized point values is 1



if __name__ == '__main__':
    # Map command line arguments to function arguments.
    makePointList(*sys.argv[1:])



















