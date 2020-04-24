from Reader import *

if __name__ == '__main__':
    # gt_path = '/Volumes/T7 Touch/School/VIP/Data/2015/LiDAR/Routes/Route2015_1'
    # useroutput_path = '/Users/danny/Downloads/UserOutput_example.csv'
    # reader = Reader()
    # gt_route = reader.createRoute(gt_path)
    # user_output = reader.collectUserSigns(useroutput_path)

    tp = 0
    tn = 0
    fp = 0
    fn = 0

    title_string = 'Pos'.center(11, " ") + 'Neg'.center(11, " ")
    print(title_string)
    string = 'T' + str(tp).center(10, " ") + '|' + str(tn).center(10, " ")
    print(string)
    print('  -------------------')
    string2 = 'F' + str(fp).center(10, " ") + '|' + str(fn).center(10, " ")
    print(string2)
    print('\n')