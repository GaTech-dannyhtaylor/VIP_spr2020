from Point import *
from GTPoint import *
from UserPoint import *
from Sign import *
from GTSign import *
from UserSign import *
from Route import *
from Reader import *
from Utilities import *
import math

import argparse

"""
This is a duplicate of Main.py. It's in function format.
"""
def main_autograder(path_to_user_output, path_to_gt):

    # Read in gt and user output data
    reader = Reader()
    gt_route = reader.createRoute(path_to_gt)
    aggregateNormGT(gt_route.sign_list)
    user_output_list = reader.collectUserSigns(path_to_user_output)

    # Set confusion matrix global variables
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    aggregate_score = 0

    # Start main loop. Find the closest GT sign and calculate IOU
    # If greater than 5, then mark UserSign as TP and GTsign.captured = yes

    for i,user_sign in enumerate(user_output_list):
        # Find closest gt sign
        min_distance = float("inf")
        min_gtsign_index = -1
        for j,gt_sign in enumerate(gt_route.sign_list):
            distance = euclidean_distance(user_sign, gt_sign)
            # print("Distance from user sign " + str(i) + " to gt_sign " + str(i) + " is: " + str(distance) + '\n')
            if distance < min_distance:
                min_distance = distance
                min_gtsign_index = j
        # print("For user sign " + str(i) + " the closest sign is gt_sign no: " + str(gt_route.sign_list[min_gtsign_index].sign_id) + " at " + str(min_distance) + " away.")
        iou = setIOU(gt_route.sign_list[min_gtsign_index], user_sign)

        # print(iou)
        if iou > 5 and gt_route.sign_list[min_gtsign_index].matched[0] == 'NO':
            tp += 1

            gt_route.num_of_matched_gt_signs += 1

            user_sign.iou = iou
            user_sign.matrix_classification = "TP"
            user_sign.matched[0] = "YES"
            user_sign.matched[1] = gt_route.sign_list[min_gtsign_index].sign_id # This is the Sign_ID of the GT sign
            user_sign.matched_ratio = tuple((user_sign.TSP_count, len(gt_route.sign_list[user_sign.matched[1]].point_list))) # This is a ratio of gt points the user captuerd to the number of total GTPoints for a sign
            
            gt_route.sign_list[min_gtsign_index].matched[0] = "YES"
            gt_route.sign_list[min_gtsign_index].matched[1] = user_sign.sign_id

            user_sign.score = scoreUserSign(user_sign)
        else:
            user_sign.matrix_classification = "FP"
            fp += 1
            # How do we score False Positives again????
            # The temporary grading is to deduct a standard amount. 10 (or -10) was the decided value
            user_sign.score = 10

    # Pump out confusion matrix. 
    # TP count comes from global variable (or the number of GTSigns that were captured or, alternatively the number of User signs that are TP)
    # FP comes from the global count (or from the number of user signs that are FP)
    # TN is always 0 right now. Perhaps this can be built out more in the future
    # FN is the number of GTsigns that were not captured
    for gt_sign in gt_route.sign_list:
        if gt_sign.matched[0] == "NO":
            fn += 1


    # Figuring out aggregate score
    # First, aggregate the NSP values 
    aggregateNSPs(user_output_list, gt_route.num_of_matched_gt_signs)

    # This will add all of the TSPspoints collected to the aggregate score and subtract all of the NSPs collected from the aggregate score
    # It will also subtract the standard deduction of false positives from the aggregate score
    for user_sign in user_output_list:
        
        if user_sign.matrix_classification == 'TP':

            for point in user_sign.point_list:
                if point.type == 'TSP':
                    aggregate_score += point.aggregateValue
                else:
                    aggregate_score -= point.aggregateValue

        elif user_sign.matrix_classification == 'FP':
            aggregate_score -= user_sign.score

    # print_confusion_matrix(tp,tn,fp,fn)
    # print('Aggregate score: %.2f' % aggregate_score)
    # print('\n')

    # for user_sign in user_output_list:
    #     if user_sign.matrix_classification == 'TP':
    #         print("Sign " + str(user_sign.sign_id) + "'s score: %.2f " % user_sign.score)
    #         print('GT points captured ratio: ' + str(user_sign.matched_ratio[0]) + '/' + str(user_sign.matched_ratio[1]))
    #         print('IOU: %.2f' % user_sign.iou)
    #         print('NSP count: ' + str(user_sign.NSP_count))
    #         print('\n')


    












    