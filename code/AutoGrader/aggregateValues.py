import math
from Point import *
from UserPoint import *
from GTPoint import *
from Sign import *
from UserSign import *
from GTSign import *


# Assigns aggregate normalized value to points in entire ground truth sign list
    #Sum each GTPoint's value, and divide each GTPoint's value by this sum
    #Afterwhich times by 100 to make total score possible for all GTPoints together to be 100
# NOTE: this method must be called after groundTruthWeight() is called which locally scores GTPoints
    #and before calling setIOU() as that is when TSP attributes are set.
def aggregateNormGT(groundTruthSignList):
    # Takes in entire ground truth sign list

    aggregateValueSum = 0

    for gtSign in groundTruthSignList:
        for gtPoint in gtSign.point_list:
            aggregateValueSum += gtPoint.value

    for gtSign in groundTruthSignList:
        for gtPoint in gtSign.point_list:
            gtPoint.aggregateValue = (gtPoint.value / aggregateValueSum) * 100

    #Testing purpose print statements:





# Assigns aggregate normalized value to points in entire user sign list
    #Sum each user NSP's value, and divide each user NSP's value by this sum
    #Afterwhich times by 100 to make total score possible for all user NSPs together to be 100 (to DEDUCT)
# NOTE: this method must be called after scoreUserSign() is called which locally scores user NSPs
def aggregateNormNSPs(userSignList):
    # Takes in list of all user signs

    aggregateValueSum = 0

    for userSign in userSignList:
        for NSP in userSign.NSP_list:
            aggregateValueSum += NSP.value

    for userSign in userSignList:
        for NSP in userSign.NSP_list:
            NSP.aggregateValue = (NSP.value / aggregateValueSum) * 100

    #Testing purpose print statements:



