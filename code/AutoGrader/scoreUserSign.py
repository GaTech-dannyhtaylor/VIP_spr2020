import math
from Point import *
from UserPoint import *
from GTPoint import *
from Sign import *
from UserSign import *
from GTSign import *

# Assign values to UserSign NSPs to score the UserSign based off its TSP and NSP values.

def scoreUserSign(gtSign, userSign):
    # Takes in the GTSign closest to the UserSign also passed
    # userSign TSPs already have value set in setIOU.py
        # Need to score NSPs of userSign

    for nsp in userSign.NSP_list:
        minDist = float("inf")
            # minDist is minimum distance from a UserPoint NSP to a GTPoint
            # initially set to infinity
        for gtPoint in gtSign.point_list:
            tempDist = (math.sqrt(((nsp.easting - gtPoint.easting)**2) + ((nsp.northing - gtPoint.northing)**2) + ((nsp.altitude - gtPoint.altitude)**2)))
            if tempDist < minDist:
                minDist = tempDist
        nsp.distance_to_closest_tsp = minDist
        if (nsp.distance_to_closest_tsp > 5) {
            nsp.value = 10
        } else {
            nsp.value = nsp.distance_to_closest_tsp / 2
        }

    # Score the userSign by summing TSPs and subtracting NSPs
    totalScore = 0
    tspScore = 0
    nspScore = 0
    for userPoint in userSign.point_list:
        if userPoint.type == "TSP":
            totalScore += userPoint.value
            tspScore += userPoint.value
        if userPoint.type == "NSP":
            totalScore -= userPoint.value
            nspScore -= userPoint.value

    userSign.score = totalScore

    #Testing purpose print statements for scoreUserSign:
    # print(f'tspScore: {tspScore}')
    # print(f'nspScore: {nspScore}')
    # print(f'userSign Score: {userSign.score}')
    # for point in userSign.TSP_list:
    #     print(f'PointID {point.point_id}, Easting {point.easting}, type {point.type}, d to GTPoint {point.distance_to_closest_tsp} value {point.value}.')
    # for point in userSign.NSP_list:
    #     print(f'PointID {point.point_id}, Easting {point.easting}, type {point.type}, d to GTPoint {point.distance_to_closest_tsp} value {point.value}.')

