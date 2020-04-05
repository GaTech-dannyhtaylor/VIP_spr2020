from Sign import * 
"""
This subclass of class Sign represents the signs in our ground truth dataset. It will contain a list of GTPoints along with all the other attributes of class 'Sign'
It will also have specific class attributes

GTSign class attribute definitions:
sign_type: String of either 'W', 'R', 'G', 'C', 'O'. These values indicate what type of signs the GT signs are
pic_frame_num: This number indicates which picture file number shows this ground truth sign

"""
class GTSign(Sign):
	
	# Constructor that takes the sign type and the pic_frame_number (these values should be found in the sign txt file).
	# You can instantiate a GTSign object with no points or pass in a list of points (either a list of GTPoints or UserPoints). 
	# Average values and centroids are calculated.
	def __init__(self, sign_id, stype, pic_frame_number, plist = []):
		self.pliist = plist
		self.sign_id = sign_id
		self.sign_type = stype
		self.pic_frame_num = pic_frame_number
