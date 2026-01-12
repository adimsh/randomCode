import math

def CSA(r, h):
    return 2*math.pi*r*h

def TSA(r, h):
    return CSA(r,h)+2*math.pi*r*r

def volume(r, h):
    return math.pi*r*r*h