

"""
This class is the parent class for TSP and NSP objects. It will hold all the meta data shared b/w TSPs and NSPs.

You can create this class with no attributes, or with some, or with all attributes. Default values for attributes are 'None'

"""
class Point:

    # Constructor for the Point class. Values do not have to be passed in to create a Point object, but they can be.
    # If not passed in on initialization, then they should be passed in afterwards
    def __init__(self, point_id = None, easting = None, northing = None, altitude = None, retro = None, angle = None, distance = None, utc = None, longitude = None, latitude = None):
        self.point_id = point_id
        self.easting = easting
        self.northing = northing
        self.altitude = altitude
        self.retro = retro
        self.angle = angle
        self.distance = distance
            # Note this distance attribute is metadata for distance point is from LiDAR gun
        self.UTC = utc
        self.longitude = longitude
        self.latitude = latitude