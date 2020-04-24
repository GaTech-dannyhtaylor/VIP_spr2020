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


# ====================================================================================================================================
    for userSign in userSignList:
        if userSign.matrix_classification == 'TP':
            for point in userSign.point_list:
                if point.type == 'NSP':
                    point.aggregateValue = point.value / num_of_matched_gt_signs
# ====================================================================================================================================



"""
Sets a userSign.iou
IOU = intersection / union
Since we are looping over all the points in a user sign, we will go ahead and set each point as a TSP or NSP and acquire the value if it's an NSP

This method will loop through and assign a user point as either a TSP or NSP. If TSP, then it copies over GT point value
If NSP, then it will calculate an NSP value based on distance from the closest GTPoint

"""

def setIOU(gtSign, userSign):
    gt_points = gtSign.point_list
    user_points = userSign.point_list
    intersection = 0

    #Loop through userSign points to check match to a GTPoint of the gtSign
    for i,userPoint in enumerate(user_points):
        found_gt_point = False
        gtIndex = 0

        while not found_gt_point and gtIndex < len(gt_points):
            if userPoint.point_id == gt_points[gtIndex].point_id:
                # Match between UserPoint and GTPoint, assign TSP and GTPoint value to UserPoint. Add to TSP_list
                userPoint.type = "TSP"
                userPoint.value = gt_points[gtIndex].value
                userPoint.aggregateValue = gt_points[gtIndex].aggregateValue
                userPoint.distance_to_closest_tsp = 0
                userSign.TSP_count += 1

                found_gt_point = True
                intersection += 1
            gtIndex += 1

        if found_gt_point == False: # You could set NSP values here aaand that's what I did
            userPoint.type = "NSP"
            userSign.NSP_count += 1
            # print(userPoint.aggregateValue)

            minDist = float("inf")
            for gtPoint in gt_points:
                tempDist = (math.sqrt(((userPoint.easting - gtPoint.easting)**2) + ((userPoint.northing - gtPoint.northing)**2) + ((userPoint.altitude - gtPoint.altitude)**2)))
                if tempDist < minDist:
                    minDist = tempDist
                userPoint.distance_to_closest_tsp = minDist
                userPoint.value = userPoint.distance_to_closest_tsp / 2

    union = len(user_points) + len(gtSign.point_list) - intersection

    # for user_point in user_points:
    #   print(user_point.type)
    #   print(str(user_point.value) + '\n')

    return 100 * (intersection / union)



# Score a user sign based on it's TSP's and NSP's

def scoreUserSign(userSign):
    # userSign TSPs already have value set in setIOU.py

    # Score the userSign by summing TSPs and subtracting NSPs
    totalScore = 0
 
    for userPoint in userSign.point_list:
        if userPoint.type == "TSP":
            totalScore += userPoint.value
        if userPoint.type == "NSP":
            totalScore -= userPoint.value

    return totalScore

