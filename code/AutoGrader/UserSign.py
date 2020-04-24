from Sign import *
"""
This subclass of class Sign represents the signs in our ground truth dataset. It will contain a list of GTPoints along with all the other attributes of class 'Sign'
It will also have specific class attributes

UserSign class attribute definitions:
sign_id: Numerical value indicating the order of the sign in the user provided route

score: Numerical value which indicates the score that the UserSign got. Acquiring TSPs will add to the score (matching GTPoints with UserPoints) and including
		NSP's (unnecessary UserPoints) will subtract from the score.

iou: Numerical value indicating the intersection of union with the closest GTSign. This is calculated later in the Autograder


"""

class UserSign(Sign):

	# Constructor that creates an empty UserSign
	# You can instantiate a GTSign object with no points or pass in a list of points (either a list of GTPoints or UserPoints). 
	# Average values and centroids are calculated.
	def __init__(self, sign_id, plist = []):
		super().__init__(plist)
		self.sign_id = sign_id
		self.score = 0
		self.iou = 0
		self.matrix_classification = ""
		self.matched = ["NO", -1] # Second element in list indicatest the sign_id of the user sign that it matched with.
		self.matched_ratio = None # This will be a tuple of the format (# of TSPs captured, # of GTpoints in matched GTSign)
		self.NSP_count = -1

		# Gabby added for iou calc
		self.TSP_list = []
		self.NSP_list = []