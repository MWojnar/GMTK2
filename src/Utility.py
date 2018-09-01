import math

def getRelativeRotation(centerRotation, targetRotation):
    while targetRotation < centerRotation - 180:
        targetRotation += 360
    while targetRotation > centerRotation + 180:
        targetRotation -= 360
    return targetRotation

def getDistance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] + pos2[1], 2))