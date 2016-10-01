import math
import mathextras


def zScore(value, average, sigma) :
    return (value - average) / sigma


def normalDistributionProbability(z) :
    return math.exp(-1*math.pow(z, 2) / 2) / math.sqrt(2 * math.pi)

def standardNorm(z, accuracy) :
    return mathextras.riemannSum(mathextras.normalDistributionProbability, 0, z, accuracy)

def mean(values):
    if len(values) == 0:
        return None
    return sum(values, 0.0) / len(values)


def standardDeviation(values, option):
    if len(values) < 2:
        return None

    sd = 0.0
    sum = 0.0
    meanValue = mean(values)

    for i in range(0, len(values)):
        diff = values[i] - meanValue
        sum += diff * diff

    sd = math.sqrt(sum / (len(values) - option))
    return sd


def stdev(values) :
    return standardDeviation(values, 1)

def stdevp(values) :
    return standardDeviation(values, 0)