# IOU = intersection / union
# Step 1: Find the intersection
# Step 2: Find the union
# Step 3:  Divid step1 by step 2
def iou(gtsign, user_sign):
	# Step 1 : Finding the intersection
	# Details: loop through each point list. 
	gt_points = gtsign.point_list
	user_points = user_sign.point_list
	matched_points = 0

	for i in range(len(user_points)):
		# Out of bounds checking
		userPoint = user_points[i]
		found = False
		counter = 0

		while not found and counter < len(gt_points):
			if userPoint.sign_id == gt_points[counter].sign_id:
				# If sign is found, break from while loop and add it to  the matched points list
				# Delete points from gtlist and userlist
				found = True
				matched_points += 1
			counter += 1

	intersection = matched_points
	union = (len(user_points) - matched_points) + (len(gt_points)- matched_points) + matched_points

	return intersection / union
				