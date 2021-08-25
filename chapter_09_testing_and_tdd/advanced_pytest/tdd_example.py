
def parameter_tdd(value):
    if value < 0:
        return 0

    if value < 10:
        return value ** 2

    return 100


assert parameter_tdd(-1) == 0
assert parameter_tdd(0) == 0
assert parameter_tdd(5) == 25
assert parameter_tdd(7) == 49
assert parameter_tdd(10) == 100
assert parameter_tdd(11) == 100
