from Reader import *

if __name__ == '__main__':
	gt_path = '/Volumes/T7 Touch/School/VIP/Data/2015/LiDAR/Routes/Route2015_1'
	useroutput_path = '/Users/danny/Downloads/UserOutput_example.csv'
	reader = Reader()
	gt_route = reader.createRoute(gt_path)
	user_output = reader.collectUserSigns(useroutput_path)