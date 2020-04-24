
"""
This class holds all the information for a route. Still undecided if this will be a parent class or not.

Starting and ending gps should be tuples
Starting and ending UTM should also be tuples
"""
class Route:

	# Constructor will all attributes as params. Initializes an empty sign list
	def __init__(self, sign_list = [], roadway = None, year = None, starting_gps = None, ending_gps = None, starting_utm = None, ending_utm = None, starting_pic_num = None, ending_pic_num = None, distance = None, num_of_signs = None, num_warning = None, num_regulatory = None, num_guide = None, num_c = None, num_other = None):
		self.sign_list = sign_list
		self.roadway = roadway
		self.year = year
		self.starting_gps = starting_gps
		self.ending_gps = ending_gps
		self.starting_utm = starting_utm
		self.ending_utm = ending_utm
		self.starting_pic_num = starting_pic_num
		self.ending_pic_num = ending_pic_num
		self.distance = distance
		self.num_of_signs = num_of_signs
		self.num_warning = num_warning
		self.num_regulatory = num_regulatory
		self.num_guide = num_guide
		self.num_c = num_c
		self.num_other = num_other
		
		self.num_of_matched_gt_signs = 0


