import sys

from scoreUserSign import *
from groundTruthWeight import *
from setIOU import *
from scoreUserSign import *

from Point import *
from UserPoint import *
from GTPoint import *
from Sign import *
from UserSign import *
from GTSign import *


def makeUserAndGTSign(userTXT, gtTXT):
    # Can run through command line: python testing.py <space separated arguments>
        # No string quotations needed for string parameters
        # /Users/Gabrielle/School/VIPLiDAR/VIP_spr2020/code/AutoGrader/testData/userSign1_2018.txt
        # /Users/Gabrielle/School/VIPLiDAR/VIP_spr2020/code/AutoGrader/testData/gtSign1_2018.txt
            # files have metadata from CloudCompare, not from Danny retain metadata script FYI

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

    userSign = UserSign(1, userPointList) #pass in sign_id and plist


    #Create GTSign
    file2 = open(gtTXT, "r")
    file2.readline()
    currRow = file2.readline()

    gtPointList = []
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
    gtSign = GTSign(1, "R", 1682, gtPointList) # pass in sign_id, stype, pic_frame_number, plist

    return [gtSign, userSign]






if __name__ == '__main__':
    # Map command line arguments to function arguments.
    pairGTUserSigns = makeUserAndGTSign(*sys.argv[1:])
    gtSign = pairGTUserSigns[0]
    userSign = pairGTUserSigns[1]

    #Assign GTPoint values for GTSign
    groundTruthWeight(gtSign)

    # Set UserSign.iou and split UserPoints into TSP_list and NSP_list. TSPs receive their value
    setIOU(gtSign, userSign)

    # Assign values to NSPs plus Sum UserSign TSP value and subtract NSP values to score UserSign
    scoreUserSign(gtSign, userSign)



















