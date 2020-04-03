from Point import *

"""
This class is a subclass of Point.py. This class represents the points that were acquired by the user. It inherits all the attributes from Point.py and
adds some TSP spectific attributes.

You can create this class with no attributes, or with some, or with all attributes. Default values for attributes are 'None'

Class Specific attribute definitions:
type = This can either be 'TSP' or 'NSP'. This indicates that this User captured point either belongs to a ground truth sign or is it not a sign point
distance_to_closest_tsp = Numerical value (meters) that measures this point's distance the closest ground truth point
value = Numerical value that either takes on a positive value is it is of type 'TSP' or a negative value if it is of type 'NSP'

"""
class UserPoint(Point):

	def __init__(self, sign_id = None, easting = None, northing = None, altitude = None, retro = None, angle = None, distance = None, utc = None, longitude = None, latitude = None):
		super().__init__(sign_id, easting, northing, altitude, retro, angle, distance, utc, longitude, latitude)
		self.type = None
		self.distance_to_closest_tsp = None
		self.value = None