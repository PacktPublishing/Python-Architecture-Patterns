
def parameter_dependent(value, sqrt_func):
    if value < 0:
        return 0

    if value <= 100:
        return sqrt_func(value)

    return 10
