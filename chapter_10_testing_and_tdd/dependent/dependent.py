import math


def parameter_dependent(value):
    if value < 0:
        return 0

    if value <= 100:
        return math.sqrt(value)

    return 10
