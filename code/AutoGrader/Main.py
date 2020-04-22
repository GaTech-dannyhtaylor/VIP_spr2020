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

if __name__ == '__main__':
	# Command line arg code
    parser = argparse.ArgumentParser(description='Input for autograder')
    parser.add_argument("--g", help = "whole path for ground truth")
    parser.add_argument("--u", help = "whole path for user output")

    args = parser.parse_args()
    gt_path = args.g
    user_output= args.u
    if gt_path is None:
        input_file = input("Enter the full path for the ground truth: ")

    if user_output is None:
        output_file = input("Enter whole path for the user output: ")

    # Read in gt and user output data
    reader = Reader()
    gt_route = reader.createRoute(gt_path)
    user_output_list = reader.collectUserSigns(user_output)

    # Set confusion matrix global variables
    tp = 0
    tn = 0
    fp = 0
    fn = 0


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

    	if iou > 5:
    		user_sign.iou = iou
    		user_sign.matrix_calssification = "TP"
    		tp += 1
    		gt_route.sign_list[min_gtsign_index].captured = "YES"
    		user_sign.score = scoreUserSign(gt_route.sign_list[min_gtsign_index], user_sign)
    		print(user_sign.score)
    	else:
    		user_sign.matrix_calssification = "FP"
    		fp += 1
    		# How do we score False Positives again????
    		user_sign.score = 0


    # Pump out confusion matrix. 
    # TP count comes from global variable (or the number of GTSigns that were captured or, alternatively the number of User signs that are TP)
    # FP comes from the global count (or from the number of user signs that are FP)
    # TN is always 0 right now. Perhaps this can be built out more in the future
    # FN is the number of GTsigns that were not captured
    for gt_sign in gt_route.sign_list:
    	if gt_sign.captured == "NO":
    		fn += 1

    print('The confusion matrix for this route is the following:\n' + 'True Positives: ' + str(tp) + '\nTrue Negatives: ' + str(tn) + '\nFalse Positives: ' + str(fp) + '\nFalse Negatives: ' + str(fn))











	