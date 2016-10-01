import math

def riemannSum(func, start, end, accuracy) :
    area = 0.0
    if accuracy == 0 :
        return 0
    width = (end-start) / accuracy
    for i in range(accuracy) :
        area += width * func(width*i)
    return area
