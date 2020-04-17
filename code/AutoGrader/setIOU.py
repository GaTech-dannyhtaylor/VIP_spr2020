# Sets a userSign.iou
    # IOU = intersection / union

# Notes for Danny, I am adding a trueGTPoint_list and NSP_list attribute for UserSign
    # changed method to set it's iou in this method

import copy
from Point import *
from UserPoint import *
from GTPoint import *
from Sign import *
from UserSign import *
from GTSign import *

def setIOU(gtSign, userSign):
    gt_points = copy.deepcopy(gtSign.point_list)
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
                # Match between UserPoint and GTPoint
                userPoint.type = "TSP"
                userPoint.distance_to_closest_tsp = 0
                TSP_list.append(gt_points[gtIndex])

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
    userSign.iou = 100 * (intersection / union) #float percent


    # Testing purpose print statements:
    # print(f'Length of userSign point list: {len(user_points)}')
    # print(f'Length of gtSign point list: {len(gtSign.point_list)}')
    # print(f'Intersection count: {intersection}')
    # print(f'Union count: {union}')
    # print(f'IOU: {userSign.iou}%')

