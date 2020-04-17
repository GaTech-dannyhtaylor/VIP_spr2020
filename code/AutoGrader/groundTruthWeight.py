import math
from Point import *
from GTPoint import *

def groundTruthWeight(gtSign):
    # Given a GTSign object, run through its point list and assign ground truth value/weight to each GTPoint
    # Weighting is inverse distance to GTSign centroid, meaning weights will decrease relative to distance from centroid
    gtPointList = gtSign.point_list

    inverseSum = 0

    for p in gtPointList:
        #Set point value intially to inverse of its distance to the centroid
        p.value = 1 / (math.sqrt(((p.easting - gtSign.centroid_easting)**2) + ((p.northing - gtSign.centroid_northing)**2) + ((p.altitude - gtSign.centroid_altitude)**2)))
        inverseSum += p.value

    for p in gtPointList:
        #Divide intial set point value by total of all point inverse centroid distance for normalization to 1
        p.value /= inverseSum
        p.value *= 100

    # Testing purpose print statements for GTSign values:
    # totalValue = 0
    # for point in gtSign.point_list:
    #     print(f'Point ID {point.point_id} of easting {point.easting} of value {point.value}.')
    #     totalValue += point.value
    # print(totalValue)     # check total of normalized point values is 100
