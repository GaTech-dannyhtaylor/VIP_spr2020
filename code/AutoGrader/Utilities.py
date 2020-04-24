from Point import *
from GTPoint import *
from UserPoint import *
from Sign import *
from GTSign import *
from UserSign import *
from Route import *
from Reader import *

import copy
import math

# This method measures the distance between two signs
def euclidean_distance(user_sign, gt_sign):
	return math.sqrt(((user_sign.centroid_easting - gt_sign.centroid_easting)**2) + ((user_sign.centroid_northing - gt_sign.centroid_northing)**2) + ((user_sign.centroid_altitude - gt_sign.centroid_altitude)**2))




# Assigns a weight to each GTPoint
def groundTruthWeight(gtSign):
    # Given a GTSign object, run through its point list and assign ground truth value/weight to each GTPoint
    # Weighting is inverse distance to GTSign centroid, meaning weights will decrease relative to distance from centroid
    gt_sign = gtSign

    inverseSum = 0

    for p in gt_sign.point_list:
        #Set point value intially to inverse of its distance to the centroid
        p.value = 1 / (math.sqrt(((p.easting - gtSign.centroid_easting)**2) + ((p.northing - gtSign.centroid_northing)**2) + ((p.altitude - gtSign.centroid_altitude)**2)))
        inverseSum += p.value

    for p in gt_sign.point_list:
        #Divide intial set point value by total of all point inverse centroid distance for normalization to 1
        p.value /= inverseSum
        p.value *= 100

    return gt_sign


# Assigns aggregate normalized value to points in entire ground truth sign list
    #Sum each GTPoint's value, and divide each GTPoint's value by this sum
    #Afterwhich times by 100 to make total score possible for all GTPoints together to be 100
# NOTE: this method must be called after groundTruthWeight() is called which locally scores GTPoints
    #and before calling setIOU() as that is when TSP attributes are set.
def aggregateNormGT(groundTruthSignList):
    # Takes in entire ground truth sign list

    aggregateValueSum = 0

    for gtSign in groundTruthSignList:
        for gtPoint in gtSign.point_list:
            aggregateValueSum += gtPoint.value

    for gtSign in groundTruthSignList:
        for gtPoint in gtSign.point_list:
            gtPoint.aggregateValue = (gtPoint.value / aggregateValueSum) * 100

    #Testing purpose print statements:



    # Testing purpose print statements for GTSign values:
    # totalValue = 0
    # for point in gtSign.point_list:
    #     print(f'Point ID {point.point_id} of easting {point.easting} of value {point.value}.')
    #     totalValue += point.value
    # print(totalValue)     # check total of normalized point values is 100



# Assigns aggregate normalized value to points in entire user sign list
    #Sum each user NSP's value, and divide each user NSP's value by this sum
    #Afterwhich times by 100 to make total score possible for all user NSPs together to be 100 (to DEDUCT)
# NOTE: this method must be called after scoreUserSign() is called which locally scores user NSPs
def aggregateNSPs(userSignList, num_of_matched_gt_signs):
    # Takes in list of all user signs

    for userSign in userSignList:
        if userSign.matrix_classification == 'TP':
        	for point in userSign.point_list:
        		if point.type == 'NSP':
        			point.aggregateValue = point.aggregateValue / num_of_matched_gt_signs




# Sets a userSign.iou
    # IOU = intersection / union

# Notes for Danny, I am adding a trueGTPoint_list and NSP_list attribute for UserSign
    # changed method to set it's userSign's iou in this method
    #also setting userPoint values that are GTpoints in this method

def setIOU(gtSign, userSign):
    gt_points = copy.deepcopy(gtSign.point_list) # Why is this a deep copy?
    user_points = userSign.point_list
    intersection = 0
    TSP_list = []
    NSP_list = []

    #Loop through userSign points to check match to a GTPoint of the gtSign
    for i in range(len(user_points)):
        userPoint = user_points[i]
        foundUserPoint = False
        gtIndex = 0

        while not foundUserPoint and gtIndex < len(gt_points):
            if userPoint.point_id == gt_points[gtIndex].point_id:
                # Match between UserPoint and GTPoint, assign TSP and GTPoint value to UserPoint. Add to TSP_list
                userPoint.type = "TSP"
                userPoint.value = gt_points[gtIndex].value
                userPoint.aggregateValue = gt_points[gtIndex].aggregateValue
                userPoint.distance_to_closest_tsp = 0
                TSP_list.append(userPoint)

                # Remove matched GTPoint from deep copy list
                gt_points.remove(gt_points[gtIndex])
                foundUserPoint = True
                intersection += 1
            gtIndex += 1

        if (foundUserPoint == False):
            userPoint.type = "NSP"
            NSP_list.append(user_points[i])

    # Assign TSP and NSP list to userSign
    userSign.TSP_list = TSP_list
    userSign.NSP_list = NSP_list

    union = len(user_points) + len(gtSign.point_list) - intersection
    # userSign.iou = 100 * (intersection / union) #float percent

    return 100 * (intersection /union)


    # Testing purpose print statements for IOU, TSP_list, NSP_list:
    # print(f'Length of userSign point list: {len(user_points)}')
    # print(f'Length of gtSign point list: {len(gtSign.point_list)}')
    # print(f'Intersection count: {intersection}')
    # print(f'Union count: {union}')
    # print(f'userSign IOU: {userSign.iou}%')
    # print(f'TSP_list length: {len(userSign.TSP_list)}')
    # print(f'NSP_list length: {len(userSign.NSP_list)}')




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
        nsp.value = nsp.distance_to_closest_tsp / 2
        # print(nsp.value)

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

    # userSign.score = totalScore

    return totalScore

    #Testing purpose print statements for scoreUserSign:
    # print(f'tspScore: {tspScore}')
    # print(f'nspScore: {nspScore}')
    # print(f'userSign Score: {userSign.score}')
    # for point in userSign.TSP_list:
    #     print(f'PointID {point.point_id}, Easting {point.easting}, type {point.type}, d to GTPoint {point.distance_to_closest_tsp} value {point.value}.')
    # for point in userSign.NSP_list:
    #     print(f'PointID {point.point_id}, Easting {point.easting}, type {point.type}, d to GTPoint {point.distance_to_closest_tsp} value {point.value}.')
