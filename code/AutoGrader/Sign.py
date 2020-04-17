"""
This is the parents class for GTSign and UserSign. It has (and subsequently passes downt through inheritance) the attributes that all signs share.

GTSign and UserSign also inherit the methods of this class. Note that in order to add points to a GTSign or a UserSign, one must call the add_points method
"""

class Sign:

    # Constructor creates a sign. You can instantiate a Sign object with no points or pass in a list of points (either a list of GTPoints or UserPoints).
    # Average values and centroids are calculated.
    def __init__(self, sign_id, plist = []):
        self.sign_id = sign_id
        self.point_list = []

        self.centroid_easting = 0
        self.centroid_northing = 0
        self.centroid_altitude = 0
        self.avg_retro = 0
        self.centroid_longitude = 0
        self.centroid_latitude = 0
        self.num_of_points = 0

        # If a list of points was passed in, then add points in list to the sign's point list and calculate centroids and average values
        if len(plist) != 0:
            self.add_points(plist)


    # This method will add either a list of points or a single point to the sign. Centroid and average values are then calculated
    # If you only want to add a single point to a sign, then just pass in the single point to the parameter 'points'
    # If you want to pass in multiple points in one method call, then put all queued points in a list and pass that list in for the variable 'points'
    def add_points(self, points):
        # If a list of points was passed in, then add all of those points to the sign's point_list.
        # Else if a single point was passed in, then add that single point to the point list
        if type(points) == list:
            for p in points:
                self.point_list.append(p)
        else:
            self.point_list.append(points)

        self.num_of_points = len(self.point_list)

        easting_total = 0
        northing_total = 0
        altitude_total = 0
        retro_total = 0
        longitude_total = 0
        latitude_total = 0

        for p in self.point_list:
            easting_total += p.easting
            northing_total += p.northing
            altitude_total += p.altitude
            retro_total += p.retro
            longitude_total += p.longitude
            latitude_total += p.latitude

        self.centroid_easting = easting_total / self.num_of_points
        self.northing_total = northing_total / self.num_of_points
        self.altitude_total = altitude_total / self.num_of_points
        self.retro_total = retro_total / self.num_of_points
        self.longitude_total = longitude_total / self.num_of_points
        self.latitude_total = latitude_total / self.num_of_points



