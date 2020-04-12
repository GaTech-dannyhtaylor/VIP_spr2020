from Point import *

"""
This class is a subclass of Point.py. This class represents the points that belong to ground truth signs. It inherits all the attributes from Point.py and
adds some TSP spectific attributes.

You can create this class with no attributes, or with some, or with all attributes. Default values for attributes are 'None'

"""
class GTPoint(Point):

	def __init__(self, point_id = None, easting = None, northing = None, altitude = None, retro = None, angle = None, distance = None, utc = None, longitude = None, latitude = None):
		super().__init__(point_id, easting, northing, altitude, retro, angle, distance, utc, longitude, latitude)
		self.value = None