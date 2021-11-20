import math
from dependent_injection import parameter_dependent


def test_good_dependency():
    assert parameter_dependent(25, math.sqrt) == 5


def test_negative():

    def bad_dependency(number):
        raise Exception('Function called')

    assert parameter_dependent(-1, bad_dependency) == 0


def test_zero():

    def good_dependency(number):
        return 0

    assert parameter_dependent(0, good_dependency) == 0


def test_twenty_five():

    def good_dependency(number):
        return 5

    assert parameter_dependent(25, good_dependency) == 5


def test_hundred():

    def good_dependency(number):
        return 10

    assert parameter_dependent(100, good_dependency) == 10


def test_hundred_and_one():

    def bad_dependency(number):
        raise Exception('Function called')

    assert parameter_dependent(101, bad_dependency) == 10
