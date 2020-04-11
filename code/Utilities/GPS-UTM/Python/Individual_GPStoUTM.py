import utm as UTM

# Quick little script to convert individual gps coordinates to UTM

if __name__ == "__main__":
	conversion = (UTM.from_latlon(float(33.91891124), float(-84.33494909)))
	print("Easting is: {}".format(conversion[0]))
	print("Northing is: {}".format(conversion[1]))